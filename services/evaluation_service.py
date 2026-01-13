from providers.groq_provider import GroqProvider
from prompts.evaluation_prompt import build_evaluation_prompt
import json

class EvaluationService:
    def __init__(self):
        self.provider = GroqProvider()

    def evaluate(self, question: str, user_answer: str, correct_answer: str):
        prompt = build_evaluation_prompt(
            question=question,
            user_answer=user_answer,
            correct_answer=correct_answer
        )

        response = self.provider.generate(prompt)

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "error": "Invalid JSON from AI",
                "raw_response": response
            }
