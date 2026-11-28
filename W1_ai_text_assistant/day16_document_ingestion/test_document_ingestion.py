import pytest
from document_ingestion import ingest_multiple_pdfs


def test_empty_pdf_paths():
    with pytest.raises(ValueError, match="PDF paths cannot be empty."):
        ingest_multiple_pdfs([])