import re

def first_word(text):
    match = re.search(r"[a-zA-Z']+", text)
    if match:
        return match.group(0)
    return ""
