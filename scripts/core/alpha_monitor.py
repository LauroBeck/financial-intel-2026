# 🏛️ Financial Intelligence Suite 2026 - Alpha Monitor
# Session Date: March 5, 2026

def calculate_session_alpha():
    # Final Close Data (Verified Mar 05, 2026)
    nasdaq_close = 22748.99
    nasdaq_pct = -0.26
    
    portfolio = {
        "IBM":  {"price": 259.16, "change": 3.64,  "tag": "Quantum/Nighthawk"},
        "TSLA": {"price": 405.55, "change": 3.44,  "tag": "Optimus/AI Event"},
        "JPM":  {"price": 293.40, "change": -2.00, "tag": "Yield Sensitivity"}
    }
    
    print(f"📊 SESSION ANALYSIS: MARCH 05, 2026")
    print(f"Benchmark (Nasdaq): {nasdaq_close} ({nasdaq_pct}%)")
    print("-" * 60)
    print(f"{'Ticker':<6} | {'Price':<8} | {'Alpha vs IXIC':<15} | {'Catalyst'}")
    print("-" * 60)
    
    for ticker, data in portfolio.items():
        # Alpha = Asset Change - Benchmark Change
        alpha = data['change'] - nasdaq_pct
        status = "🟢" if alpha > 0 else "🔴"
        print(f"{ticker:<6} | ${data['price']:>7.2f} | {status} {alpha:>+6.2f}% | {data['tag']}")

if __name__ == "__main__":
    calculate_session_alpha()
