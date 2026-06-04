#!/usr/bin/env python3
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("❌ PIL (Pillow) is not installed. Installing it via pip first...")
    print("   Please run: pip install Pillow")
    sys.exit(1)

theme_dir = os.path.dirname(os.path.abspath(__file__))

def fix_icons():
    icons_dir = os.path.join(theme_dir, "icons")
    icon1_path = os.path.join(icons_dir, "icon-48.png")
    icon2_path = os.path.join(icons_dir, "icon-96.png")
    root_source_path = os.path.join(theme_dir, "dolphin_park_icon_source.png")
    old_source_path = os.path.join(icons_dir, "dolphin_park_icon_source.png")
    
    # Ensure icons directory exists
    os.makedirs(icons_dir, exist_ok=True)
    
    # 1. Handle auto-migration of old source icon to the root directory
    if os.path.exists(old_source_path) and not os.path.exists(root_source_path):
        import shutil
        shutil.move(old_source_path, root_source_path)
        print("📦 Migrated high-res original icon to root: dolphin_park_icon_source.png")
    
    # 2. If it's already moved but the old one is still lingering, delete it
    if os.path.exists(old_source_path):
        os.remove(old_source_path)
        print("🧹 Cleaned up old source icon from icons/ folder")

    # 3. If root source does not exist, find a backup candidate from existing icons
    if not os.path.exists(root_source_path):
        import shutil
        if os.path.exists(icon1_path):
            shutil.copy2(icon1_path, root_source_path)
            print("📦 Backed up high-res original icon to root: dolphin_park_icon_source.png")
        elif os.path.exists(icon2_path):
            shutil.copy2(icon2_path, root_source_path)
            print("📦 Backed up high-res original icon to root: dolphin_park_icon_source.png")
        else:
            print("❌ No icon files found to optimize!")
            return False
            
    print("📐 Resizing icons to correct manifest specifications...")
    try:
        # Resize 48x48 icon
        with Image.open(root_source_path) as img:
            img_48 = img.resize((48, 48), Image.Resampling.LANCZOS)
            img_48.save(icon1_path, format="PNG")
            print("✅ Resized icons/icon-48.png to 48x48 px")
            
        # Resize 96x96 icon
        with Image.open(root_source_path) as img:
            img_96 = img.resize((96, 96), Image.Resampling.LANCZOS)
            img_96.save(icon2_path, format="PNG")
            print("✅ Resized icons/icon-96.png to 96x96 px")
            
        return True
    except Exception as e:
        print(f"❌ Failed to resize icons: {e}")
        return False

if __name__ == "__main__":
    print("🛠️ DolphinPark Asset Optimizer")
    print("=============================")
    icons_ok = fix_icons()
    if icons_ok:
        print("\n🎉 All assets optimized and resized successfully!")
    else:
        print("\n⚠️ Some assets could not be optimized. See errors above.")
