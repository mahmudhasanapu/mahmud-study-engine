def build_summary_prompt(text: str) -> str:
    return f"""
Summarize the following notes in short, clear bullet points.

Rules:
- Include all important points
- Keep sentences concise
- No extra explanation
- Return valid JSON only

Format:
{{
  "summary": [
    "Point 1",
    "Point 2",
    "Point 3"
  ]
}}

Notes:
{text}
"""
