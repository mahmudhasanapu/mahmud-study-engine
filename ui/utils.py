# ui/utils.py

import json

def parse_ai_output(raw_text: str) -> dict:
    """
    AI থেকে আসা raw text কে parse করে JSON dictionary বানায়
    যদি valid JSON না হয়, তাহলে error dict return করে
    """
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        # AI ঠিকঠাক JSON দেয়নি
        return {
            "error": "Invalid JSON",
            "raw_output": raw_text
        }
