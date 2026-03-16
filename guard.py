from shadow_guard.patterns import SENSITIVE_PATTERNS
from shadow_guard.notifier import alert_user
from shadow_guard.monitor import ClipboardMonitor

if __name__ == "__main__":
    monitor = ClipboardMonitor(SENSITIVE_PATTERNS, alert_user)
    monitor.start()