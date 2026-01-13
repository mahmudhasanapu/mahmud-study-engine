from config.settings import GROQ_API_KEY
from groq import Groq  # Correct import

class GroqProvider:
    def __init__(self):
        # Initialize Groq client
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, prompt: str) -> str:
        # ChatCompletion call to Groq
        response = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="openai/gpt-oss-20b",  #একটা supported model (example) :contentReference[oaicite:2]{index=2}
        )
        # Return text content
        return response.choices[0].message.content
