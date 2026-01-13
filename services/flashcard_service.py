from providers.groq_provider import GroqProvider
from prompts.flashcard_prompt import build_flashcard_prompt
from ui.utils import parse_ai_output

class FlashcardService:
    def __init__(self):
        self.provider = GroqProvider()  

    def generate_flashcards(self, text: str) -> dict:
        prompt = build_flashcard_prompt(text) 
        raw = self.provider.generate(prompt)   
        return parse_ai_output(raw)   
