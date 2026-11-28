from document_ingestion import ingest_multiple_pdfs


def main():
    pdf_paths = [
        "sample_pdfs/scorereport.pdf",
        "sample_pdfs/machine_learning.pdf",
        "sample_pdfs/fastapi.pdf"
    ]

    all_documents = ingest_multiple_pdfs(pdf_paths)

    print("========== MULTIPLE PDF INGESTION ==========")
    print("Total pages ingested:", len(all_documents))

    for document in all_documents:
        print("\nDocument:", document["document"])
        print("Page:", document["page"])
        print("Text preview:", document["text"][:50])


if __name__ == "__main__":
    main()