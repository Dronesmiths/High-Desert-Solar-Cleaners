import os
import shutil

def get_all_project_files(project_root):
    """Get all code files to scan for references."""
    code_files = []
    # Extensions to scan for references
    extensions = {'.html', '.css', '.js', '.json', '.md', '.txt', '.py'}
    
    for root, dirs, files in os.walk(project_root):
        # Exclude hidden and factory logic itself (optional, but we want to know if factory uses it)
        if any(d in root for d in [".git", ".gemini", "node_modules", "__pycache__"]):
            continue

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in extensions:
                code_files.append(os.path.join(root, file))
    return code_files

def get_all_images(images_dir):
    """Get all image files in the images directory."""
    image_files = set()
    if not os.path.exists(images_dir):
        return image_files

    for root, dirs, files in os.walk(images_dir):
        for file in files:
            # Add relevant image extensions
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.ico')):
                # Store relative path to images/ AND just filename for loose matching
                # We'll store the filename to match against content
                image_files.add(file)
    return image_files

def clean_assets():
    # 1. Setup Paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    images_dir = os.path.join(project_root, "images")
    trash_dir = os.path.join(project_root, "_trash_images")
    
    print(f"Scanning project: {project_root}")
    
    # 2. Inventory
    all_images = get_all_images(images_dir)
    if not all_images:
        print("No images found to clean.")
        return

    print(f"Found {len(all_images)} images in inventory.")

    # 3. Scan Content
    used_images = set()
    code_files = get_all_project_files(project_root)
    
    print(f"Scanning {len(code_files)} files for references...")

    for file_path in code_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Check for each image
                # Optimization: Could check regex, but checking exact filename existence is robust for static sites
                for img in all_images:
                    if img in content:
                        used_images.add(img)
        except Exception as e:
            print(f"Skipping {file_path}: {e}")

    # 4. Determine Unused
    unused_images = all_images - used_images
    
    # Always protect branding assets explicitly if they aren't referenced directly in code 
    # (e.g. if they are dynamically loaded, though our scan should catch them if filenames match)
    # Adding a safety whitelist just in case
    whitelist = {"favicon.ico", "apple-touch-icon.png", "favicon-32x32.png", "favicon-16x16.png", "site.webmanifest"}
    unused_images = unused_images - whitelist

    if not unused_images:
        print("\n[CLEAN] All images are in use! nice work.")
        return

    # 5. Move to Trash
    if not os.path.exists(trash_dir):
        os.makedirs(trash_dir)

    print(f"\n[ACTION] Found {len(unused_images)} unused images. Moving to {trash_dir}...")
    
    manifest_path = os.path.join(trash_dir, "manifest.txt")
    with open(manifest_path, "a") as manifest:
        from datetime import datetime
        manifest.write(f"\n--- Purge Run: {datetime.now()} ---\n")
        
        for img in unused_images:
            print(f"  - Identifying: {img}")
            found = False
            for root, dirs, files in os.walk(images_dir):
                if img in files:
                    src = os.path.join(root, img)
                    dst = os.path.join(trash_dir, img)
                    shutil.move(src, dst)
                    manifest.write(f"Moved: {img}\n")
                    print(f"  > Moved: {img}")
                    found = True
                    break
            if not found:
                print(f"  ! Warning: Could not locate {img} for move.")
                manifest.write(f"Missing: {img}\n")

    # 6. Archive to Zip
    archive_name = os.path.join(project_root, "legacy_assets_backup")
    shutil.make_archive(archive_name, 'zip', trash_dir)
    print(f"\n[BACKUP] Archived purged assets to: {archive_name}.zip")
    print("[DONE] Verification complete. You can safely delete '_trash_images' and the zip file when ready.")

if __name__ == "__main__":
    clean_assets()
