
import pymupdf
from pathlib import Path


def extract_pdf_pages(pdf_path):
    # Validate input
    if not isinstance(pdf_path, (str, Path)):
        raise ValueError("PDF path must be a string or Path.")

    pdf_path = Path(pdf_path)
    print(f"Extracting pages from: {pdf_path}")

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if not pdf_path.is_file():
        raise ValueError("Provided path is not a file.")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("File must have a PDF extension.")

    pages = []

    # Open and extract PDF
    with pymupdf.open(pdf_path) as doc:

        for page_number, page in enumerate(doc, start=1):
            text = page.get_text().strip()

            if not text:
                continue

            pages.append({
                "page": page_number,
                "text": text
            })

    return pages

