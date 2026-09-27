import re

INJECTION_PATTERNS=(r'ignore .*instructions',r'system prompt',r'developer message',r'reveal .*prompt')

def contains_injection(text):
    return any(re.search(p,text.lower()) for p in INJECTION_PATTERNS)

def sanitize(text):
    return '[UNTRUSTED DOCUMENT INSTRUCTION OMITTED]' if contains_injection(text) else text
