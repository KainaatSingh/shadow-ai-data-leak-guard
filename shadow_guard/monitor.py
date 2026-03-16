# shadow_guard/monitor.py

import pyclip
import time
import re

class ClipboardMonitor:
    def __init__(self, patterns, notifier_func):
        self.patterns = patterns
        self.alert_user = notifier_func

    def start(self):
        print("🛡️ Shadow Guard is active... (Press Ctrl+C to stop)")
        last_paste = ""
        
        while True:
            try:
                # Get current clipboard content
                current_paste = pyclip.paste().decode('utf-8')
                
                if current_paste != last_paste:
                    # Check against our 'Illegal' list
                    for label, pattern in self.patterns.items():
                        if re.search(pattern, current_paste):
                            # BUSTED! Clear it immediately
                            pyclip.copy("") 
                            self.alert_user(label)
                            print(f"!!! BLOCKED: {label}")
                            current_paste = "" # Reset local variable
                            break
                    
                    last_paste = current_paste
            except pyclip.base.ClipboardSetupException:
                pass
            except Exception as e:
                # Sometimes clipboard is empty or has an image; we ignore those errors
                pass
                
            time.sleep(0.5) # Check every half-second
