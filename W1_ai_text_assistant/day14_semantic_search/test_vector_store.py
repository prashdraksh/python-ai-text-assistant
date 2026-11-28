
import pytest
from vector_store import VectorStore


@pytest.fixture
def store(tmp_path):
    return VectorStore(db_path=str(tmp_path))


def test_add_documents(store):
    documents = [
        {
            "id": "test_001",
            "text": "Python is a programming language.",
            "metadata": {"category": "programming", "page": 1}
        }
    ]

    embeddings = [[0.1, 0.2, 0.3]]

    store.add_documents(documents, embeddings)

    assert store.collection.count() == 1


def test_add_documents_mismatched_count(store):
    documents = [
        {
            "id": "test_001",
            "text": "Python is a programming language.",
            "metadata": {"category": "programming", "page": 1}
        }
    ]

    embeddings = []

    with pytest.raises(ValueError):
        store.add_documents(documents, embeddings)


def test_search_invalid_top_k(store):
    with pytest.raises(ValueError):
        store.search([0.1, 0.2, 0.3], top_k=0)


def test_search_returns_matching_category(store):
    documents = [
        {
            "id": "test_001",
            "text": "Python programming.",
            "metadata": {"category": "programming", "page": 1}
        },
        {
            "id": "test_002",
            "text": "Machine learning.",
            "metadata": {"category": "machine_learning", "page": 2}
        }
    ]

    embeddings = [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6]
    ]

    store.add_documents(documents, embeddings)

    results = store.search(
        query_embedding=[0.4, 0.5, 0.6],
        top_k=2,
        category="machine_learning"
    )

    assert results["ids"][0] == ["test_002"]
