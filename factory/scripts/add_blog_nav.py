
import os

search_markers = [
    '<li><a href="/about/">About Us</a></li>',
    '<li><a href="/services/">Services</a></li>',
    '<li><a href="/">Home</a></li>'
]
nav_item = '                    <li><a href="/news/">News</a></li>'

def update_nav(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if '/blog/' in content:
        print(f"Blog link already exists in {filepath}")
        return

    found_marker = False
    for marker in search_markers:
        if marker in content:
            new_content = content.replace(marker, marker + '\n' + nav_item)
            found_marker = True
            break
    
    if not found_marker:
        print(f"Could not find any nav markers in {filepath}")
        return
    
    # Handle active state for blog page itself (though manually created, good practice)
    if 'blog' in filepath:
        new_content = new_content.replace('href="/blog/"', 'href="/blog/" class="active"')
        
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Updated nav in {filepath}")

def main():
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".gemini" in root or "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                update_nav(os.path.join(root, file))

if __name__ == "__main__":
    main()
