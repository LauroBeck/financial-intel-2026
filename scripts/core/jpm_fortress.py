# JPM Fortress Monitor - Created 2026-03-05
TICKER = "JPM"
PRICE_ACTUAL = 293.59
DIV_YIELD_TTM = "1.98%"
CET1_RATIO_TARGET = 0.155  # 15.5%

def monitor_fortress_health(current_cet1):
    if current_cet1 >= CET1_RATIO_TARGET:
        return "STABLE: Fortress intact."
    else:
        return "ALERT: Capital buffer narrowing."

print(f"JPM Asset Status: {monitor_fortress_health(0.162)}")
