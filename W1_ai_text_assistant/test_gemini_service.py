
from dotenv import load_dotenv
from llm_service import create_gemini_client
from main import run_assistant

load_dotenv()

client = create_gemini_client()

text = """
Python is a popular programming language.
It is used in web development, automation,
data science and artificial intelligence.
"""

result = run_assistant(
    client=client,
    text=text,
    task="extract"
)

print("\n========== AI TEXT ASSISTANT ==========")
print("Answer:", result["answer"])
print("Keywords:", result["keywords"])
