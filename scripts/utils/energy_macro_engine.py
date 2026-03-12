# ==========================================
# BLOOMBERG ENERGY SHOCK MACRO ENGINE
# Author: Lauro Beck
# Project: Financial Intel 2026
# ==========================================

import pandas as pd


# ==========================================
# 1. OIL SHOCK DETECTOR
# ==========================================

class OilShockDetector:

    def __init__(self):
        self.threshold = 5  # % move defining macro shock

    def detect_shock(self, df):

        avg_move = df["ChangePct"].mean()

        if avg_move > 10:
            regime = "EXTREME_OIL_SPIKE"
        elif avg_move > self.threshold:
            regime = "OIL_SUPER_SPIKE"
        elif avg_move > 2:
            regime = "OIL_BULLISH"
        else:
            regime = "NORMAL"

        return regime, avg_move


# ==========================================
# 2. ENERGY EQUITY BETA MODEL
# ==========================================

class EnergyBetaModel:

    def __init__(self):

        self.beta = {
            "Chevron": 0.65,
            "ExxonMobil": 0.60,
            "Halliburton": 0.85,
            "BakerHughes": 0.80,
            "BP": 0.58
        }

    def project_returns(self, oil_move):

        results = {}

        for company, sensitivity in self.beta.items():

            gain = oil_move * sensitivity
            results[company] = round(gain, 2)

        return pd.DataFrame.from_dict(
            results, orient="index", columns=["ProjectedGain%"]
        )


# ==========================================
# 3. GLOBAL TRADE MOMENTUM MODEL
# ==========================================

class GlobalTradeMomentum:

    def compute_index(self, oil_move):

        trade_index = (
            oil_move * 0.4 +   # shipping demand
            oil_move * 0.2 +   # petrochemicals
            oil_move * 0.3 +   # refining margins
            oil_move * 0.1     # global logistics
        )

        return round(trade_index, 2)


# ==========================================
# 4. MAIN EXECUTION ENGINE
# ==========================================

def main():

    # Brent futures snapshot (Bloomberg style)
    brent_data = {
        "Contract": ["May26", "Jun26", "Jul26", "Aug26"],
        "Price": [107.00, 99.32, 92.81, 88.06],
        "ChangePct": [15.44, 13.90, 11.98, 10.27]
    }

    df = pd.DataFrame(brent_data)

    print("\nBRENT FUTURES SNAPSHOT\n")
    print(df)

    # Detect oil shock
    detector = OilShockDetector()
    regime, shock = detector.detect_shock(df)

    # Energy stock projections
    energy_model = EnergyBetaModel()
    projections = energy_model.project_returns(shock)

    # Global trade momentum
    trade_model = GlobalTradeMomentum()
    trade_index = trade_model.compute_index(shock)

    print("\n====================================")
    print("BLOOMBERG ENERGY SHOCK MODEL")
    print("====================================\n")

    print("Oil Market Regime:", regime)
    print("Average Brent Shock:", round(shock, 2), "%\n")

    print("Projected Energy Equity Gains\n")
    print(projections)

    print("\nGlobal Trade Momentum Index:", trade_index)

    print("\n====================================\n")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()
