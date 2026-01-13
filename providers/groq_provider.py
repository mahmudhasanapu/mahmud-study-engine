from config.settings import GROQ_API_KEY
from groq import Groq  

class GroqProvider:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="openai/gpt-oss-20b",  
        )
        return response.choices[0].message.content
