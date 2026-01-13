def build_evaluation_prompt(question: str, user_answer: str, correct_answer: str) -> str:
    return f"""
You are an answer evaluator.

Evaluate the user's answer based on the correct answer.

Rules:
- Give a score from 0 to 5
- Say if the answer is correct or incorrect
- Give short, clear feedback
- Return ONLY valid JSON
- Do NOT add markdown or explanation

Output format:
{{
  "is_correct": true or false,
  "score": number,
  "feedback": "short feedback"
}}

Question:
{question}

Correct Answer:
{correct_answer}

User Answer:
{user_answer}
"""
