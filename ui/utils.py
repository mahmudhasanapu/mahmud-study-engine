import json

def parse_ai_output(raw_text: str) -> dict:
 
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON",
            "raw_output": raw_text
        }
