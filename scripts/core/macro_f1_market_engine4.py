# ==========================================
# GLOBAL MACRO + F1 SENTIMENT ENGINE
# Author: Lauro Beck
# Project: Financial Intel 2026
# ==========================================

import pandas as pd
import yfinance as yf


# ==========================================
# MARKET DATA ENGINE (LIVE INTRADAY)
# ==========================================

class MarketDataEngine:

    def fetch_prices(self):

        tickers = {
            "SP500": "^GSPC",
            "NASDAQ100": "^NDX",
            "BRENT": "BZ=F",
            "GOLD": "GC=F",
            "USD": "DX-Y.NYB",
            "MICROSOFT": "MSFT"
        }

        results = {}

        for name, ticker in tickers.items():

            try:

                data = yf.download(
                    ticker,
                    period="1d",
                    interval="1m",
                    progress=False
                )

                if data.empty:
                    raise ValueError("No market data")

                if isinstance(data.columns, pd.MultiIndex):
                    close_series = data["Close"][ticker]
                    open_series = data["Open"][ticker]
                else:
                    close_series = data["Close"]
                    open_series = data["Open"]

                price_now = float(close_series.iloc[-1])
                open_price = float(open_series.iloc[0])

                change = ((price_now - open_price) / open_price) * 100

                results[name] = round(change, 2)

            except Exception as e:

                print(f"Data error for {name}: {e}")
                results[name] = 0.0

        return results


# ==========================================
# MACRO PROPAGATION MODEL
# ==========================================

class MacroPropagationModel:

    def __init__(self):

        self.beta = {
            "NasdaqMomentum": 1.25,
            "DefenseSector": 0.75,
            "EnergySector": 0.55,
            "GoldReaction": -0.35,
            "USDReaction": -0.25
        }

    def propagate(self, sp_move):

        predictions = {}

        for asset, sensitivity in self.beta.items():

            move = sp_move * sensitivity
            predictions[asset] = round(move, 2)

        return predictions


# ==========================================
# OIL SHOCK ADJUSTMENT
# ==========================================

class OilShockAdjustment:

    def adjust(self, predictions, oil_move):

        oil_move = float(oil_move)

        print("\nOil Move Detected:", oil_move, "%")

        if oil_move > 5:

            print("⚠ OIL SHOCK DETECTED")

            predictions["EnergySector"] += round(oil_move * 0.4, 2)
            predictions["DefenseSector"] += round(oil_move * 0.3, 2)

        return predictions


# ==========================================
# MACRO REGIME DETECTOR
# ==========================================

class MacroRegime:

    def detect(self, sp_move, oil_move):

        if sp_move > 1 and oil_move > 5:
            return "ENERGY WAR SHOCK"

        elif sp_move > 1:
            return "RISK ON"

        elif sp_move < -1:
            return "RISK OFF"

        else:
            return "NEUTRAL"


# ==========================================
# F1 SENTIMENT ENGINE
# ==========================================

class F1SentimentEngine:

    def mercedes_sentiment(self, result):

        sentiment = 0

        if result == "MERCEDES_1_2":
            sentiment = 0.6

        elif result == "MERCEDES_WIN":
            sentiment = 0.4

        elif result == "PODIUM":
            sentiment = 0.2

        return sentiment


# ==========================================
# TECH IMPACT MODEL (MICROSOFT / NASDAQ)
# ==========================================

class TechImpactModel:

    def compute(self, sp_move, sentiment):

        nasdaq_projection = sp_move * 1.25
        microsoft_projection = nasdaq_projection + sentiment

        return {
            "NasdaqProjection": round(nasdaq_projection, 2),
            "MicrosoftMomentum": round(microsoft_projection, 2)
        }


# ==========================================
# MAIN ENGINE
# ==========================================

def main():

    print("\n=================================")
    print("GLOBAL MACRO + F1 MARKET ENGINE")
    print("=================================\n")

    # Get live market data
    data_engine = MarketDataEngine()
    market = data_engine.fetch_prices()

    df = pd.DataFrame.from_dict(market, orient="index", columns=["Move%"])

    print("MARKET SNAPSHOT\n")
    print(df)
    print("\n")

    sp_move = float(market.get("SP500", 0))
    oil_move = float(market.get("BRENT", 0))

    # Macro regime
    regime_detector = MacroRegime()
    regime = regime_detector.detect(sp_move, oil_move)

    # Macro propagation
    macro_model = MacroPropagationModel()
    predictions = macro_model.propagate(sp_move)

    # Oil shock
    oil_adjust = OilShockAdjustment()
    predictions = oil_adjust.adjust(predictions, oil_move)

    # F1 sentiment scenario
    race_result = "MERCEDES_1_2"

    f1_engine = F1SentimentEngine()
    sentiment = f1_engine.mercedes_sentiment(race_result)

    tech_model = TechImpactModel()
    tech_projection = tech_model.compute(sp_move, sentiment)

    print("\nMACRO REGIME:", regime)

    print("\nMACRO PROPAGATION FORECAST\n")

    for asset, move in predictions.items():
        print(asset, "->", move, "%")

    print("\nF1 TECH SENTIMENT\n")

    print("Race Result:", race_result)
    print("Sentiment Boost:", sentiment)

    print("\nTECH MARKET PROJECTION\n")

    for k, v in tech_projection.items():
        print(k, "->", v, "%")

    print("\n=================================\n")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()
