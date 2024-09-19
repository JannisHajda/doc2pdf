# 📄 doc2pdf
Convert your **doc, docx, ppt, pptx**, and more to **PDF** with ease using this simple Docker application! Perfect for those needing batch conversion without the hassle of installing software on your local machine.

![](docker.gif)

## ✨ Features
- **Batch Conversion**: Convert multiple files at once, maintaining folder structure.
- **Supported Formats**: .doc, .docx, .odt, .ppt, .pptx, .odp.
- **Headless Operation**: Powered by LibreOffice in headless mode, everything happens behind the scenes.

## 🚀 Quick Start Guide
1. Install Docker and Docker Compose on your system.
2. Input Files: Place your doc, docx, ppt, pptx, odt, or odp files inside the `input` directory.
3. Fonts: Add any required custom fonts to the ```fonts``` directory.
4. Conversion: Run the container (`docker compose up`), and your converted PDFs will be available inside the `output`directory, preserving the same folder structure as your input.

<br>
⭐ If you found this repo useful, please consider giving a star!