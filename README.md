# 🐬 DolphinPark — Firefox Theme

> Wave Race 64 energy. Sunny aqua lagoon. Bright, breezy, readable.
> Built by Nyx Aetherlink / VoidLabs Designs

---

## Vibe

Crystal turquoise lagoon on a perfect summer day. Think Wave Race 64 Dolphin Park —
bright tropical blues, sun sparkling off the water, crisp white foam. Cheerful, light,
and readable at a glance.

**Pairs with:** DeepAbyss theme (the dark mode counterpart in this collection; website coming soon).

---

## Color Palette

| Token                        | Hex       | Role                            |
| ---------------------------- | --------- | ------------------------------- |
| `frame`                      | `#0096c7` | Chrome bg — bright ocean blue   |
| `frame_inactive`             | `#48cae4` | Inactive window — lighter aqua  |
| `toolbar`                    | `#90e0ef` | Nav bar — sky blue              |
| `tab_selected`               | `#caf0f8` | Active tab — near-white aqua    |
| `tab_text`                   | `#03045e` | Active tab text — deep navy     |
| `tab_background_text`        | `#023e8a` | Inactive tab text — dark blue   |
| `tab_line`                   | `#0077b6` | Tab accent underline            |
| `toolbar_field`              | `#ffffff`  | URL bar bg — white              |
| `toolbar_field_text`         | `#03045e` | URL bar text — deep navy        |
| `toolbar_field_border`       | `#48cae4` | URL bar border — aqua           |
| `toolbar_field_border_focus` | `#0096c7` | URL bar focus ring              |
| `toolbar_text`               | `#03045e` | Toolbar text/icons              |
| `icons`                      | `#0077b6` | Toolbar icons                   |
| `icons_attention`            | `#ff6b35` | Bookmarks/downloads — orange    |
| `popup`                      | `#e0f4fd` | Context menus — pale aqua       |
| `popup_text`                 | `#03045e` | Menu text — deep navy           |

---

## File Structure

```text
Dolphin_Park_Theme/
├── manifest.json              ← Theme definition
├── dolphin_park_icon_source.png ← High-res source icon
├── icons/
│   ├── icon-48.png            ← Dolphin icon (48x48 px)
│   └── icon-96.png            ← Same (scaled copy, 96x96 px)
└── README.md                  ← This file
```

---

## 📦 Setup & Packaging

Since the repository is focused purely on source assets, the final package is compiled locally:

1. Ensure the assets are in place:
   * Icons: `icons/icon-48.png` and `icons/icon-96.png` (generated from `dolphin_park_icon_source.png`)

2. Compile the extension (produces `dolphin_park_theme.xpi`):

   ```bash
   chmod +x install.sh
   ./install.sh
   ```

---

## 🔌 Installation

### Temporary (Testing)

1. Navigate to `about:debugging` in Firefox.
2. Click **This Firefox** -> **Load Temporary Add-on...**
3. Select the `manifest.json` file in this directory.

### Permanent

1. Drag and drop the generated `dolphin_park_theme.xpi` into any open Firefox tab.
2. Confirm the installation prompt.

*(Note: Requires setting `xpinstall.signatures.required` to `false` in `about:config` on Firefox Developer Edition/Nightly).*

---

## Customization

| What to change   | Property          | Current     |
| ---------------- | ----------------- | ----------- |
| Tab accent line  | `tab_line`        | `#0077b6`   |
| Toolbar shade    | `toolbar`         | `#90e0ef`   |
| Frame saturation | `frame`           | `#0096c7`   |
| Attention icons  | `icons_attention` | `#ff6b35`   |
