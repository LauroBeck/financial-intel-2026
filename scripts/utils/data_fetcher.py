import yfinance as yf
import pandas as pd

def get_market_snapshot(tickers=["IBM", "TSLA", "JPM", "^IXIC"]):
    print(f"📡 Fetching Mar 05 2026 Closing Data...")
    try:
        data = yf.download(tickers, period="1d")['Close']
        return data.iloc[-1]
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    snapshot = get_market_snapshot()
    print(snapshot)
