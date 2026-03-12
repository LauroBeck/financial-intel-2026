import nasdaqdatalink
import os

nasdaqdatalink.ApiConfig.api_key = os.getenv("NASDAQ_API_KEY")

# Fetching the NASDAQ Composite Index from FRED (Updated to March 2026)
print("🚀 Fetching actual 2026 NASDAQ Index levels...")
try:
    # 'FRED/NASDAQCOM' is the code for the Nasdaq Composite
    data = nasdaqdatalink.get("FRED/NASDAQCOM", rows=10)
    print("\n--- Recent Nasdaq Levels (2026) ---")
    print(data)
except Exception as e:
    print(f"Error: {e}")
