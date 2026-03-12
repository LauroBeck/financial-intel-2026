import os
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from datetime import datetime

# IBM Terminal Style
plt.style.use('dark_background')
IBM_BLUE = '#0f62fe'

def analyze_trend(data_series):
    """Calculates 2nd derivative acceleration for inflection points."""
    arr = data_series.values
    smooth = gaussian_filter1d(arr, sigma=2)
    accel = np.gradient(np.gradient(smooth))
    # Detect where acceleration crosses zero (The Inflection)
    infl_pts = np.where(np.diff(np.sign(accel)))[0]
    return smooth, accel, infl_pts

def run_ibm_env_monitor():
    print(f"\n🏛️  IBM STRATEGIC MONITOR | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}")

    # 1. Fetching 2026 Data
    tickers = ["IBM", "^IXIC"]
    try:
        # 2026 yfinance requires multi_level_index=False for clean column access
        data = yf.download(tickers, period="3mo", interval="1d", multi_level_index=False)
        ibm_raw = data['Close']['IBM'].dropna()
        nas_raw = data['Close']['^IXIC'].dropna()
    except Exception as e:
        print(f"❌ Data Error: {e}")
        return

    # 2. Mathematical Analysis
    ibm_s, ibm_a, ibm_i = analyze_trend(ibm_raw)
    
    # 3. Market Intelligence
    current_px = ibm_raw.iloc[-1]
    current_accel = ibm_a[-1]
    status = "🚀 ACCELERATING" if current_accel > 0 else "📉 DECELERATING"
    
    print(f"IBM PRICE:   ${current_px:.2f}")
    print(f"STATUS:      {status}")
    print(f"NAS COMP:    {nas_raw.iloc[-1]:.2f} (Tech Sell-off Risk)")
    print(f"{'-'*60}")

    # 4. Professional Visualization
    plt.figure(figsize=(12, 6))
    plt.plot(ibm_raw.index, ibm_raw, color=IBM_BLUE, lw=2.5, label='IBM (Value Recovery)')
    plt.plot(ibm_raw.index, ibm_s, color='white', linestyle='--', alpha=0.4, label='Trend')
    
    # Mark Inflection Points
    plt.scatter(ibm_raw.index[ibm_i], ibm_raw.iloc[ibm_i], 
                color='red', s=80, edgecolors='white', zorder=5, label='Inflection Pt')

    plt.title("IBM VS NASDAQ: 2026 DECOUPLING ANALYSIS", loc='left', fontsize=12)
    plt.legend()
    plt.grid(alpha=0.1)
    
    os.makedirs('research', exist_ok=True)
    plt.savefig('research/ibm_inflection_2026.png')
    print(f"📈 Chart archived to: research/ibm_inflection_2026.png")

if __name__ == "__main__":
    run_ibm_env_monitor()
