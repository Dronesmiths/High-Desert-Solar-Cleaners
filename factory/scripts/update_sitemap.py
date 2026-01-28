import os
import json
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

def load_config():
    """Load configuration from factory_config.json"""
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "factory_config.json"))
    if not os.path.exists(config_path):
        print(f"ERROR: Configuration file not found at {config_path}")
        sys.exit(1)
    
    with open(config_path, 'r') as f:
        return json.load(f)

def update_sitemap():
    config = load_config()
    client = config.get("client", {})
    DOMAIN = client.get("domain", "example.com")
    
    # 1. Base Project Root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    sitemap_path = os.path.join(project_root, "sitemap.xml")
    
    ET.register_namespace('', "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    if os.path.exists(sitemap_path):
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
    else:
        # Create fresh if missing
        root = ET.Element("urlset")
        root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
        tree = ET.ElementTree(root)

    # 2. Scan for HTML files
    urls = set()
    for child in root:
        loc = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc is not None:
            urls.add(loc.text)

    # 3. Walk directory
    new_urls_count = 0
    today = datetime.now().strftime("%Y-%m-%d")

    for root_dir, dirs, files in os.walk(project_root):
        if any(d in root_dir for d in [".git", ".gemini", "node_modules", "factory"]):
            continue
            
        for file in files:
            if file == "index.html":
                # Calculate URL
                rel_path = os.path.relpath(root_dir, project_root)
                if rel_path == ".":
                    url = f"https://{DOMAIN}/"
                    priority = "1.0"
                else:
                    url = f"https://{DOMAIN}/{rel_path}/"
                    priority = "0.8" if "services" in rel_path else "0.7"
                    if "blog" in rel_path:
                        priority = "0.6"

                if url not in urls:
                    new_url = ET.SubElement(root, "url")
                    ET.SubElement(new_url, "loc").text = url
                    ET.SubElement(new_url, "lastmod").text = today
                    ET.SubElement(new_url, "priority").text = priority
                    print(f"Added: {url}")
                    new_urls_count += 1
                    urls.add(url)

    if new_urls_count > 0:
        # Indent XML
        ET.indent(tree, space="  ", level=0)
        tree.write(sitemap_path, encoding="UTF-8", xml_declaration=True)
        print(f"Sitemap updated with {new_urls_count} new URLs.")
    else:
        print("Sitemap is already up to date.")

if __name__ == "__main__":
    update_sitemap()
