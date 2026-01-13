from providers.groq_provider import GroqProvider
from prompts.summary_prompt import build_summary_prompt
from ui.utils import parse_ai_output

class SummaryService:
    def __init__(self):
        self.provider = GroqProvider()

    def generate_summary(self, text: str) -> dict:
        prompt = build_summary_prompt(text)
        raw = self.provider.generate(prompt)
        return parse_ai_output(raw)
