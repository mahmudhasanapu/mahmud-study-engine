# services/flashcard_service.py

from providers.groq_provider import GroqProvider
from prompts.flashcard_prompt import build_flashcard_prompt
from ui.utils import parse_ai_output  # এখানে helper ব্যবহার করলাম

class FlashcardService:
    def __init__(self):
        self.provider = GroqProvider()  # AI call provider

    def generate_flashcards(self, text: str) -> dict:
        prompt = build_flashcard_prompt(text)  # Prompt বানানো
        raw = self.provider.generate(prompt)   # AI call
        return parse_ai_output(raw)            # JSON-safe parse
