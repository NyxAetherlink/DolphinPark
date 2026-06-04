#!/usr/bin/env fish
# DolphinPark Firefox Theme - Install Script
# Usage: fish install.sh

set THEME_DIR (dirname (status --current-filename))

echo "🐬 DolphinPark Theme Installer"
echo "------------------------------"

# Create icons directory
mkdir -p $THEME_DIR/icons

# Check for icon
if not test -f "$THEME_DIR/icons/icon-48.png"
    echo "❌ Missing: icons/icon-48.png"
    echo "   Copy the generated icon image to: $THEME_DIR/icons/icon-48.png"
    exit 1
end

# Create 96px icon as copy of 48px if missing
if not test -f "$THEME_DIR/icons/icon-96.png"
    cp "$THEME_DIR/icons/icon-48.png" "$THEME_DIR/icons/icon-96.png"
    echo "✅ Created icons/icon-96.png from icon-48.png"
end

echo "✅ All assets present"

# Package as .xpi (just a zip with .xpi extension)
cd $THEME_DIR
set XPI_PATH "$THEME_DIR/dolphin_park_theme.xpi"

zip -r /tmp/dolphin_park_theme.zip manifest.json icons/
mv /tmp/dolphin_park_theme.zip $XPI_PATH

echo "✅ Packaged: $XPI_PATH"
echo ""
echo "📦 To install temporarily (for testing):"
echo "   1. Open Firefox → about:debugging"
echo "   2. Click 'This Firefox' → 'Load Temporary Add-on...'"
echo "   3. Select: $THEME_DIR/manifest.json"
echo ""
echo "📦 To install permanently (drag & drop):"
echo "   Drag dolphin_park_theme.xpi into a Firefox window"
