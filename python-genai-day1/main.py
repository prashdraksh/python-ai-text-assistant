
# # # from prompts import prepare_prompt
# # # from llm_service import FakeLLMClient, generate_response


# # # def main():
# # #     text = input("Enter your text: ")
# # #     task = input("Choose task (summarize/explain/extract): ")

# # #     try:
# # #         prompt = prepare_prompt(text, task)

# # #         print("\nGenerated Prompt:")
# # #         print(prompt)

# # #         client = FakeLLMClient()
# # #         result = generate_response(client, prompt)

# # #         print(f"\nAI Response: {result}")

# # #     except ValueError as exc:
# # #         print(f"\nInput Error: {exc}")

# # #     except RuntimeError as exc:
# # #         print(f"\nService Error: {exc}")


# # # if __name__ == "__main__":
# # #     main()

# # from response_parser import parse_response

# # response_data = {
# #     "id": "response_123",
# #     "status": "completed",
# #     "output_text": "     Machine learning enables computers to learn from data."
# # }

# # result = parse_response(response_data)

# # print(result)


# # from prompt_builder import build_messages

# # document = """
# # Machine learning is a branch of artificial intelligence
# # that enables systems to learn from data.
# # """

# # question = "What is machine learning?"

# # messages = build_messages(document, question)

# # print("SYSTEM INSTRUCTIONS:")
# # print(messages["instructions"])

# # print("\nUSER MESSAGE:")
# # print(messages["input"])

# from token_utils import check_output_limit

# response = "Python is a popular programming language."

# try:
#     count = check_output_limit(response, 10)
#     print(f"Estimated tokens: {count}")
# except ValueError as exc:
#     print(exc)

from structured_parser import parse_json_response

response_text = """
{
    "title": "Python Basics",
    "author": "John",
    "summary": "Introduction to Python programming.",
    "keywords": ["Python", "Programming"]
}
"""

data = parse_json_response(response_text)

print("Title:", data["title"])
print("Author:", data["author"])
print("Summary:", data["summary"])
print("Keywords:", data["keywords"])