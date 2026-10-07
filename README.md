<p align="center">
  <img src="https://img.shields.io/badge/python-3-3776AB?logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/OCR-Tesseract-5A5A5A" alt="Tesseract OCR">
  <img src="https://img.shields.io/badge/status-private-red" alt="status: private">
</p>

# hw

**A homework workspace for turning scanned Filipino literature readings into text you can search, and writing analyses of them.**

Class readings often come as scanned PDFs, so you cannot search them or copy
from them. This repo runs OCR on a reading, saves the text it reads, and keeps
the written analysis next to the source.

What is in it now:

- **Hudhud ni Aliguyon** (Castro et al.): the scanned PDF, its pages as images
  in `pdf_pages/`, the OCR text in `output.txt`, and a bilingual Filipino–English
  analysis in [`Komprehensibong_Pagsusuri_Hudhud_ni_Aliguyon.md`](Komprehensibong_Pagsusuri_Hudhud_ni_Aliguyon.md).
- [`ocr_pdf_to_text.py`](ocr_pdf_to_text.py): the OCR script that produced `output.txt`.

## Quick start

```bash
brew install tesseract poppler          # Tesseract does the OCR; poppler is what pdf2image needs
pip install pytesseract pdf2image Pillow
python ocr_pdf_to_text.py               # writes output.txt
```

To OCR a different reading, change the PDF filename passed to
`convert_from_path(...)` and the output filename in the script.

## Configuration

None. There is no `.env`.

## How it works

```
scanned PDF ──pdf2image (300 dpi)──▶ page images ──pytesseract──▶ output.txt
                                                                  │
                                                       analysis written in Markdown
```
