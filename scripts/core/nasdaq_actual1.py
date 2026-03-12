# Nasdaq Composite Actuals
INDEX_VALUE = 22684.66
DAILY_CHANGE = -0.54
VOL_MILLIONS = 650.70

def log_alert(msg):
    with open("nasdaq_alerts.log", "a") as f:
        f.write(f"2026-03-05: {msg}\n")

if DAILY_CHANGE < -0.50:
    log_alert(f"Volatility Spike: Nasdaq dipped to {INDEX_VALUE}")
