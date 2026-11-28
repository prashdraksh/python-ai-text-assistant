
import pytest
from pdf_loader import extract_pdf_pages


def test_extract_pdf_pages():
    pages = extract_pdf_pages("scorereport.pdf")

    assert len(pages) == 2
    assert pages[0]["page"] == 1
    assert pages[1]["page"] == 2
    assert pages[0]["text"] != ""


def test_missing_pdf():
    with pytest.raises(FileNotFoundError):
        extract_pdf_pages("missing.pdf")


def test_invalid_extension(tmp_path):
    text_file = tmp_path / "sample.txt"
    text_file.write_text("This is not a PDF.")

    with pytest.raises(ValueError):
        extract_pdf_pages(text_file)


def test_invalid_input_type():
    with pytest.raises(ValueError):
        extract_pdf_pages(123)
