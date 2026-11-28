
import pytest
from vector_store import VectorStore


@pytest.fixture
def vector_store(tmp_path):
    return VectorStore(db_path=str(tmp_path / "test_db"))


def sample_chunks():
    return [
        {
            "chunk_id": "chunk_001",
            "document": "sample.pdf",
            "page": 1,
            "text": "Python is a programming language."
        },
        {
            "chunk_id": "chunk_002",
            "document": "sample.pdf",
            "page": 2,
            "text": "Machine learning learns from data."
        }
    ]


def test_add_chunks(vector_store):
    chunks = sample_chunks()
    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]

    vector_store.add_chunks(chunks, embeddings)

    assert vector_store.collection.count() == 2


def test_mismatched_chunks_and_embeddings(vector_store):
    chunks = sample_chunks()
    embeddings = [[1.0, 0.0, 0.0]]

    with pytest.raises(ValueError):
        vector_store.add_chunks(chunks, embeddings)


def test_search_with_page_filter(vector_store):
    chunks = sample_chunks()
    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]

    vector_store.add_chunks(chunks, embeddings)

    results = vector_store.search(
        query_embedding=[0.0, 1.0, 0.0],
        top_k=3,
        page=2
    )

    assert results["ids"][0] == ["chunk_002"]
    assert results["metadatas"][0][0]["page"] == 2


def test_invalid_top_k(vector_store):
    with pytest.raises(ValueError):
        vector_store.search(
            query_embedding=[1.0, 0.0, 0.0],
            top_k=0
        )


def test_search_with_document_filter(vector_store):
    chunks = sample_chunks()
    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]

    vector_store.add_chunks(chunks, embeddings)

    results = vector_store.search(
        query_embedding=[1.0, 0.0, 0.0],
        top_k=3,
        document="sample.pdf"
    )

    assert len(results["ids"][0]) == 2

    for metadata in results["metadatas"][0]:
        assert metadata["document"] == "sample.pdf"


def test_search_with_combined_filters(vector_store):
    chunks = sample_chunks()
    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]

    vector_store.add_chunks(chunks, embeddings)

    results = vector_store.search(
        query_embedding=[0.0, 1.0, 0.0],
        top_k=3,
        page=2,
        document="sample.pdf"
    )

    assert results["ids"][0] == ["chunk_002"]


def test_search_no_matching_page(vector_store):
    chunks = sample_chunks()
    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ]

    vector_store.add_chunks(chunks, embeddings)

    results = vector_store.search(
        query_embedding=[1.0, 0.0, 0.0],
        top_k=3,
        page=99
    )

    assert results["ids"][0] == []
