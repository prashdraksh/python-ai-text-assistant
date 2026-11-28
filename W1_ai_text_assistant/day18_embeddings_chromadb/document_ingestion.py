
from pathlib import Path
from pdf_loader import extract_pdf_pages


def ingest_pdf(pdf_path):
    pdf_path = Path(pdf_path)

    pages = extract_pdf_pages(pdf_path)

    documents = []

    for page in pages:
        documents.append({
            "document": pdf_path.name,
            "page": page["page"],
            "text": page["text"]
        })

    return documents


def ingest_multiple_pdfs(pdf_paths):
    if not pdf_paths:
        raise ValueError("PDF paths cannot be empty.")
    
    all_documents = []

    for pdf_path in pdf_paths:
        documents = ingest_pdf(pdf_path)
        all_documents.extend(documents)

    return all_documents
