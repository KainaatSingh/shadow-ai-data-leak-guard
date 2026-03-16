import pyclip
import time
import re
from plyer import notification

# 1. Define 'Illegal' patterns (Regex)
SENSITIVE_PATTERNS = {
    "OpenAI API Key": r"sk-[a-zA-Z0-9]{48}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Generic Password": r"(?i)password\s*[:=]\s*[^\s]+", # Matches 'password: mysecret'
    "Email Address": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
}

def alert_user(label):
    notification.notify(
        title="🔒 Data Leak Blocked",
        message=f"Detected {label}. Clipboard has been cleared.",
        timeout=5
    )

def monitor_clipboard():
    print("🛡️ Shadow Guard is active... (Press Ctrl+C to stop)")
    last_paste = ""
    
    while True:
        try:
            # Get current clipboard content
            current_paste = pyclip.paste().decode('utf-8')
            
            if current_paste != last_paste:
                # Check against our 'Illegal' list
                for label, pattern in SENSITIVE_PATTERNS.items():
                    if re.search(pattern, current_paste):
                        # BUSTED! Clear it immediately
                        pyclip.copy("") 
                        alert_user(label)
                        print(f"!!! BLOCKED: {label}")
                        current_paste = "" # Reset local variable
                        break
                
                last_paste = current_paste
                
        except Exception as e:
            # Sometimes clipboard is empty or has an image; we ignore those errors
            pass
            
        time.sleep(0.5) # Check every half-second

if __name__ == "__main__":
    monitor_clipboard()