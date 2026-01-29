import os
import re
import sys
import json

def load_config():
    """Load configuration from factory_config.json"""
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "factory_config.json"))
    if not os.path.exists(config_path):
        print(f"ERROR: Configuration file not found at {config_path}")
        sys.exit(1)
    
    with open(config_path, 'r') as f:
        return json.load(f)

def print_banner(text):
    print("\n" + "="*60)
    print(f" {text}")
    print("="*60)

def audit_files(directory, config):
    errors = 0
    warnings = 0
    
    # Extract config values
    client = config.get("client", {})
    aws = config.get("aws", {})
    seo = config.get("seo", {})
    
    CLIENT_NAME = client.get("name", "[BUSINESS_NAME]")
    PHONE = client.get("phone", "[PHONE_NUMBER]")
    # Clean phone for regex/search
    RAW_PHONE = re.sub(r'\D', '', PHONE)
    
    FORBIDDEN_WORDS = ["Diaz Landscaping", "Diaz", "LER", "Reed and Sons", "Artisan Bread", "Handyman", "AV Pool Bros", "Pool Bros"]
    
    html_files = []
    for root, dirs, files in os.walk(directory):
        if any(d in root for d in [".git", ".gemini", "node_modules", "factory"]):
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    print(f"Auditing {len(html_files)} HTML files for brand integrity ({CLIENT_NAME})...")

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, directory)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        file_issues = []

        # 1. Leakage Check
        for word in FORBIDDEN_WORDS:
            # Use word boundaries for stricter matching
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, content, re.IGNORECASE) and word.lower() != CLIENT_NAME.lower():
                file_issues.append(f"CRITICAL: Found legacy branding/forbidden word '{word}'")
                errors += 1

        # 2. Identity Sync
        if PHONE not in content and "tel:" in content:
            # Check for any phone numbers that don't match our RAW_PHONE
            found_phones = re.findall(r'tel:(\d{10,11})', content)
            if found_phones and found_phones[0] != RAW_PHONE:
                 file_issues.append(f"WARNING: Phone number mismatch. Found {found_phones[0]}, expected {RAW_PHONE}")
                 warnings += 1

        # 3. Broken Links / Placeholders
        if 'href="#"' in content:
            file_issues.append("WARNING: Found placeholder link href='#'")
            warnings += 1
            
        # 4. Meta Quality & Social
        if "<title>" not in content:
            file_issues.append("ERROR: Missing <title> tag")
            errors += 1

        if 'name="description"' not in content:
            file_issues.append("WARNING: Missing meta description")
            warnings += 1

        if file_issues:
            print(f"\n[!] {rel_path}:")
            for issue in file_issues:
                print(f"  - {issue}")

    return errors, warnings

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    config = load_config()
    
    client_name = config.get("client", {}).get("name", "Unknown Client")
    print_banner(f"FACTORY PRE-FLIGHT AUDIT: {client_name}")
    
    err, warn = audit_files(project_root, config)
    
    print_banner("AUDIT SUMMARY")
    print(f"Total Errors: {err}")
    print(f"Total Warnings: {warn}")
    
    if err > 0:
        print("\n[RESULT] FAIL: Critical errors found. Do not deploy.")
        sys.exit(1)
    else:
        print("\n[RESULT] PASS: System is ready for deployment sync.")
        sys.exit(0)
