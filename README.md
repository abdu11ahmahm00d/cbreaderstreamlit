# Comic Book Reader (Streamlit) 📚

> A comic book (CBR/CBZ) reader built with Streamlit.

Upload `.cbr` or `.cbz` files and browse pages with navigation controls.

## Features

- **Format Support** — CBR (RAR) and CBZ (ZIP) archives
- **Page Navigation** — Previous/next buttons + direct page input
- **Image Extraction** — Auto-extracts JPG/PNG from archives
- **Sidebar Controls** — Go-to-page and navigation sidebar

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Streamlit |
| Archive | rarfile, zipfile |
| Images | Pillow (PIL) |

## Known Limitations

- Temp directory management needs improvement
- Best suited for small to medium comic files

## Quick Start

```bash
pip install streamlit pillow rarfile
streamlit run index.py
```
