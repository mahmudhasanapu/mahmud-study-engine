def build_flashcard_prompt(text: str) -> str:
    return f"""
Generate exactly 5 flashcards from the text below.

Rules:
- Each flashcard must have one question and one answer
- Questions short and clear
- Answers short and correct
- Do NOT add extra explanation
- Return valid JSON only

Return format:
{{
  "flashcards": [
    {{"question": "Question 1", "answer": "Answer 1"}}
  ]
}}

Text:
{text}
"""
