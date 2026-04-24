# Save as JPG — ComfyUI Custom Node

A lightweight **ComfyUI custom node** that saves images as **JPEG (.jpg)** files with configurable quality and optional caption sidecar files.

⚠️ This node is a **small fork derived from** the project:  
https://github.com/kijai/ComfyUI-KJNodes

The code was simplified and adapted to provide a minimal standalone **Save as JPG** node.

---

# Features

- Save ComfyUI images directly as **.jpg**
- Adjustable **JPEG quality**
- Optional **JPEG optimization**
- Supports **relative or absolute output folders**
- Optional **caption sidecar files** (`.txt` or other extensions)
- Compatible with **ComfyUI filename numbering**
- Handles **RGBA → RGB conversion automatically**
- **Concurrent generation safe** - automatically prevents file overwrites by incrementing filenames when conflicts occur

---

# Installation

1. Navigate to your ComfyUI `custom_nodes` directory:

---

# License

This project is licensed under the **GNU Affero General Public License v3.0**.
See the [LICENSE](LICENSE) file for the full text.
