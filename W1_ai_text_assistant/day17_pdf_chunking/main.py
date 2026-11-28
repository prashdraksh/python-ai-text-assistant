from document_ingestion import ingest_pdf
from document_chunker import chunk_documents


def main():

    pdf_path = "sample_pdfs/documind_sample_3_pages.pdf"

    # Step 1: Extract PDF pages
    documents = ingest_pdf(pdf_path)

    # Step 2: Convert pages into chunks
    chunks = chunk_documents(
        documents,
        chunk_size=50,
        overlap=10
    )

    print("========== PDF CHUNKING RESULTS ==========")

    print("Total pages:", len(documents))
    print("Total chunks:", len(chunks))

    for chunk in chunks:

        print("\nChunk ID:", chunk["chunk_id"])
        print("Document:", chunk["document"])
        print("Page:", chunk["page"])
        print("Text:", chunk["text"][:150])


if __name__ == "__main__":
    main()