# Install dependencies:
# pip install pytesseract pdf2image Pillow
# Also install Tesseract OCR: https://github.com/tesseract-ocr/tesseract

import pytesseract
from pdf2image import convert_from_path

# Convert PDF pages to images
pages = convert_from_path("1.5 Mga Epiko ng Pilipinas Hudhud ni Aliguyon (Castro, et al.) (1).pdf", dpi=300)

all_text = ""
for i, page in enumerate(pages):
    print(f"Processing page {i + 1}/{len(pages)}...")
    text = pytesseract.image_to_string(page)
    all_text += f"\n--- Page {i + 1} ---\n{text}"

# Save to a text file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"Done! Extracted text from {len(pages)} pages.")
