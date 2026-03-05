import yfinance as yf

def get_snapshot(tickers=["IBM", "TSLA", "JPM", "^IXIC"]):
    """Fetches latest available close for 2026 session monitoring."""
    print("📡 Ingesting live market feed...")
    try:
        data = yf.download(tickers, period="1d")['Close']
        return data.iloc[-1]
    except Exception as e:
        return f"Fetch Error: {e}"

if __name__ == "__main__":
    print(get_snapshot())
