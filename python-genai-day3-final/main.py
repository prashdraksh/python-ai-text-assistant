
from dotenv import load_dotenv

from prompt_builder import build_messages
from llm_service import create_gemini_client, generate_response
from structured_parser import parse_json_response


def main():
    load_dotenv()

    document = """
    Machine learning is a branch of artificial intelligence
    that enables computers to learn patterns from data.
    """

    question = input("Ask a question about the document: ")

    try:
        messages = build_messages(document, question)

        client = create_gemini_client()

        raw_response = generate_response(
            client,
            messages,
            max_output_tokens=200
        )

        result = parse_json_response(raw_response)

        print("\nAI Answer:")
        print(result["answer"])

        print("\nKeywords:")
        for keyword in result["keywords"]:
            print("-", keyword)

        client.close()

    except ValueError as exc:
        print(f"\nInput or configuration error: {exc}")

    except Exception as exc:
        print(f"\nGemini API error: {exc}")


if __name__ == "__main__":
    main()








# from prompt_builder import build_messages
# from llm_service import FakeLLMClient, generate_response
# from structured_parser import parse_json_response


# def main():
#     document = """
#     Machine learning is a branch of artificial intelligence
#     that enables computers to learn patterns from data.
#     """

#     question = input("Ask a question about the document: ")

#     try:
#         # Step 1: Build messages
#         messages = build_messages(document, question)

#         # Step 2: Create LLM client
#         client = FakeLLMClient()

#         # Step 3: Generate response
#         raw_response = generate_response(
#             client,
#             messages,
#             temperature=0.2,
#             max_output_tokens=200
#         )

#         # Step 4: Parse JSON response
#         result = parse_json_response(raw_response)

#         # Step 5: Display result
#         print("\nAI Answer:")
#         print(result["answer"])

#         print("\nKeywords:")
#         for keyword in result["keywords"]:
#             print("-", keyword)

#     except ValueError as exc:
#         print(f"\nInput or response error: {exc}")

#     except Exception as exc:
#         print(f"\nUnexpected service error: {exc}")


# if __name__ == "__main__":
#     main()
