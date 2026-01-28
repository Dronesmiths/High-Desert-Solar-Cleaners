import os
import sys
from PIL import Image

def generate_favicons(source_image_path):
    if not os.path.exists(source_image_path):
        print(f"Error: Source image not found at {source_image_path}")
        return

    img = Image.open(source_image_path)
    
    # 1. Standard ICO (includes 16, 32, 48)
    img.save("images/favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print("Generated: images/favicon.ico")
    
    # 2. PNG Sizes
    sizes = {
        "favicon-16x16.png": (16, 16),
        "favicon-32x32.png": (32, 32),
        "apple-touch-icon.png": (180, 180),
        "android-chrome-192x192.png": (192, 192),
        "android-chrome-512x512.png": (512, 512)
    }
    
    for filename, size in sizes.items():
        resized = img.resize(size, Image.Resampling.LANCZOS)
        resized.save(f"images/{filename}")
        print(f"Generated: images/{filename}")

    # 3. Main Logo & Social Share
    # Standard logo (matches footer usage)
    logo_size = (400, 150) # Maintain aspect ratio if possible, but for now fit to box
    img.thumbnail(logo_size, Image.Resampling.LANCZOS)
    img.save("images/av-pool-bros-logo.png")
    print("Generated: images/av-pool-bros-logo.png")

    img.save("images/logo-og.png")
    print("Generated: images/logo-og.png")

if __name__ == "__main__":
    # Assumes running from project root or checks factory asset
    # Default to Looking for logo in factory/brand_assets
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    os.chdir(project_root) # Switch to project root
    
    # Try multiple sources
    sources = [
        "factory/brand_assets/authoritative-logo.png",
        "factory/brand_assets/PLACEHOLDER_LOGO.png",
        "images/av-pool-bros-logo.png" 
    ]
    
    selected_source = None
    for src in sources:
        if os.path.exists(src):
            selected_source = src
            break
            
    if selected_source:
        print(f"Generating favicons from: {selected_source}")
        generate_favicons(selected_source)
    else:
        print("No suitable source logo found in factory/brand_assets/ or images/")
