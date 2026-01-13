from providers.groq_provider import GroqProvider
from prompts.quiz_prompt import build_quiz_prompt
from ui.utils import parse_ai_output

class QuizService:
    def __init__(self):
        self.provider = GroqProvider()

    def generate_quiz(self, text: str) -> dict:
        prompt = build_quiz_prompt(text)
        raw = self.provider.generate(prompt)
        return parse_ai_output(raw)
