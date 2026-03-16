# shadow_guard/notifier.py

from plyer import notification

def alert_user(label):
    notification.notify(
        title="🔒 Data Leak Blocked",
        message=f"Detected {label}. Clipboard has been cleared.",
        timeout=5
    )
