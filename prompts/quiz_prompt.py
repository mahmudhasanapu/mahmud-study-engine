def build_quiz_prompt(text: str) -> str:
    return f"""
Generate exactly 5 multiple-choice questions (MCQs) from the text below.

Rules:
- 4 options per question (A, B, C, D)
- Clearly mark correct answer
- No extra text
- Return valid JSON only

Format:
{{
  "quiz": [
    {{
      "question": "Question here",
      "options": {{
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D"
      }},
      "correct_answer": "A"
    }}
  ]
}}

Text:
{text}
"""
