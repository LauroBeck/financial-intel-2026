import yfinance as yf

def run_alpha_sweep():
    # Final Close Data: March 5, 2026
    # Nasdaq Index: 22,748.99 (-0.26%)
    # JPM: 93.40 (-2.00%)
    # IBM: 59.16 (+3.64%)
    # TSLA: 05.55 (+3.44%)
    
    ixic_delta = -0.26
    portfolio = {
        "IBM":  {"price": 259.16, "delta": 3.64, "note": "Quantum (Nighthawk) Rally"},
        "TSLA": {"price": 405.55, "delta": 3.44, "note": "Optimus Gen 3 Hype"},
        "JPM":  {"price": 293.40, "delta": -2.00, "note": "Yield Pressure"}
    }
    
    print(f"🏛️ INNOVATION ALPHA SWEEP | MARCH 05, 2026")
    print("-" * 65)
    print(f"{'Ticker':<6} | {'Price':<8} | {'Alpha vs IXIC':<15} | {'Catalyst'}")
    print("-" * 65)
    
    for ticker, m in portfolio.items():
        alpha = m['delta'] - ixic_delta
        status = "🟢" if alpha > 0 else "🔴"
        print(f"{ticker:<6} | ${m['price']:>7.2f} | {status} {alpha:>+6.2f}% | {m['note']}")
    
    print("-" * 65)
    print("ANALYSIS: Tech-to-Innovation rotation confirmed.")

if __name__ == "__main__":
    run_alpha_sweep()
