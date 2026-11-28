
from pdf_loader import extract_pdf_pages


def main():
    pdf_path = "scorereport.pdf"

    pages = extract_pdf_pages(pdf_path)

    print("PDF extraction successful!")
    print("Total extracted pages:", len(pages))

    for page in pages:
        print("\n========== PAGE", page["page"], "==========")
        print(page["text"][:200])


if __name__ == "__main__":
    main()
