# shadow_guard/patterns.py

# 1. Define 'Illegal' patterns (Regex)
SENSITIVE_PATTERNS = {
    "OpenAI API Key": r"sk-[a-zA-Z0-9]{48}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Generic Password": r"(?i)password\s*[:=]\s*[^\s]+", # Matches 'password: mysecret'
    "Email Address": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
}
