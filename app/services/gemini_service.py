from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ Define client properly
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def classify_intent(email_text: str) -> str:
    try:
        prompt = f"""
        Classify the intent of this email into one of:
        - scheduling
        - summarization
        - other

        Email:
        {email_text}

        Only return one word.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if response.text:
            return response.text.strip().lower()
        else:
            return "other"

    except Exception as e:
        print("Gemini Error:", e)
        return "other"