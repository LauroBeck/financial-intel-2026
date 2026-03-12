import pandas as pd
import random

print("\n=================================")
print("GLOBAL MACRO MARKET ENGINE PRO")
print("=================================\n")


# ---------------------------
# MARKET DATA INPUT
# ---------------------------

market = {
    "SP500": 0.82,
    "NASDAQ100": 1.10,
    "RUSSELL2000": 0.55,
    "BRENT": 16.65,
    "GOLD": -1.46,
    "VIX": -2.30
}


stocks = {
    "Microsoft": 1.40,
    "Nvidia": 2.10,
    "Apple": 0.95
}


# ---------------------------
# F1 SENTIMENT ENGINE
# ---------------------------

def f1_sentiment():

    # Mercedes positive innovation sentiment
    mercedes_win = True

    if mercedes_win:
        sentiment = 0.35
        print("🏎 F1 Sentiment: Mercedes strong result -> Tech optimism")
    else:
        sentiment = -0.15
        print("🏎 F1 Sentiment: Neutral")

    return sentiment


# ---------------------------
# OIL SHOCK DETECTION
# ---------------------------

def oil_shock(oil_move):

    if oil_move > 10:
        print("\n⚠ OIL SHOCK DETECTED")
        return 1
    else:
        return 0


# ---------------------------
# MACRO PROPAGATION MODEL
# ---------------------------

def macro_propagation():

    sp = market["SP500"]
    nasdaq = market["NASDAQ100"]
    russell = market["RUSSELL2000"]
    oil = market["BRENT"]
    gold = market["GOLD"]
    vix = market["VIX"]

    msft = stocks["Microsoft"]
    nvda = stocks["Nvidia"]
    aapl = stocks["Apple"]

    f1 = f1_sentiment()
    oil_flag = oil_shock(oil)

    print("\nMARKET SNAPSHOT\n")

    df = pd.DataFrame({
        "Move%": market
    })

    print(df)

    print("\nMEGA CAP MOVES\n")

    df2 = pd.DataFrame({
        "Move%": stocks
    })

    print(df2)

    # ---------------------------
    # PROPAGATION LOGIC
    # ---------------------------

    nasdaq_momentum = nasdaq + (msft + nvda + aapl) / 6 + f1

    energy_sector = oil * 0.35 + oil_flag * 2

    defense_sector = oil * 0.15 + 0.8

    gold_reaction = gold + (vix * -0.2)

    usd_reaction = oil * 0.02 + vix * 0.03

    small_cap_flow = russell + sp * 0.3

    ai_sector = nvda * 0.8 + msft * 0.6 + f1

    volatility_regime = vix * -0.5 + sp * 0.2

    # ---------------------------
    # OUTPUT
    # ---------------------------

    results = {
        "NasdaqMomentum": round(nasdaq_momentum,2),
        "EnergySector": round(energy_sector,2),
        "DefenseSector": round(defense_sector,2),
        "GoldReaction": round(gold_reaction,2),
        "USDReaction": round(usd_reaction,2),
        "SmallCapFlow": round(small_cap_flow,2),
        "AISector": round(ai_sector,2),
        "VolatilityRegime": round(volatility_regime,2)
    }

    print("\nMACRO PROPAGATION FORECAST\n")

    for k,v in results.items():
        print(k,"->",v,"%")



# ---------------------------
# RUN ENGINE
# ---------------------------

macro_propagation()


print("\n=================================\n")
