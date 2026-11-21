from dotenv import load_dotenv
from llm_service import create_gemini_client

load_dotenv()

print("Creating client...")
client = create_gemini_client()

print("Sending simple request...")

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Reply with exactly: Gemini connection works."
)

print("Response received:")
print(response.text)