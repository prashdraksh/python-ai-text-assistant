import pytest
from document_chunker import chunk_documents


def test_chunk_documents():
    documents = [
        {
            "document": "sample.pdf",
            "page": 1,
            "text": " ".join(["Python"] * 120)
        }
    ]

    chunks = chunk_documents(
        documents,
        chunk_size=50,
        overlap=10
    )

    assert len(chunks) == 3
    assert chunks[0]["page"] == 1
    assert chunks[0]["document"] == "sample.pdf"
    assert chunks[0]["chunk_id"] == "sample.pdf_1_chunk_1"
    assert len(chunks[0]["text"].split()) == 50


def test_empty_documents():
    with pytest.raises(ValueError, match="Documents cannot be empty."):
        chunk_documents([])