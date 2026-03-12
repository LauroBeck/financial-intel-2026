import sys
import cv2
import pytesseract
import pandas as pd
import re

# -----------------------------
# OCR IMAGE
# -----------------------------

def run_ocr(image_path):

    img = cv2.imread(image_path)

    if img is None:
        print("❌ File not found:", image_path)
        sys.exit()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    thresh = cv2.adaptiveThreshold(
        gray,255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,31,2
    )

    text = pytesseract.image_to_string(thresh)

    return text


# -----------------------------
# CLEAN OCR TEXT
# -----------------------------

def clean_text(text):

    text = text.lower()

    text = text.replace("\n"," ")

    text = re.sub(r'[^a-z0-9.$% ]',' ',text)

    text = re.sub(r'\s+',' ',text)

    return text


# -----------------------------
# SMART KEYWORD DETECTION
# -----------------------------

def detect_macro(text):

    signals = {
        "war":0,
        "oil":0,
        "inflation":0,
        "jobs":0,
        "gold":0,
        "volatility":0
    }

    war_words = [
        "war","conflict","iran","attack",
        "military","missile","middle east"
    ]

    oil_words = [
        "oil","crude","brent","energy"
    ]

    inflation_words = [
        "inflation","rates","interest rates","fed"
    ]

    jobs_words = [
        "jobs","payroll","unemployment"
    ]

    gold_words = [
        "gold"
    ]

    vol_words = [
        "volatility","vix","fear"
    ]

    for w in war_words:
        if w in text:
            signals["war"] += 1

    for w in oil_words:
        if w in text:
            signals["oil"] += 1

    for w in inflation_words:
        if w in text:
            signals["inflation"] += 1

    for w in jobs_words:
        if w in text:
            signals["jobs"] += 1

    for w in gold_words:
        if w in text:
            signals["gold"] += 1

    for w in vol_words:
        if w in text:
            signals["volatility"] += 1

    return signals


# -----------------------------
# MACRO REGIME MODEL
# -----------------------------

def macro_regime(signals):

    score = 0

    score += signals["war"] * 3
    score += signals["oil"] * 2
    score += signals["inflation"] * 2
    score += signals["volatility"] * 3
    score -= signals["jobs"] * 1

    if score >= 6:
        return "RISK OFF / WAR SHOCK"

    if score >= 3:
        return "GEOPOLITICAL STRESS"

    if score <= -2:
        return "RISK ON"

    return "NEUTRAL"


# -----------------------------
# SECTOR FORECAST
# -----------------------------

def sector_forecast(signals):

    energy = signals["oil"] * 3 + signals["war"] * 2
    defense = signals["war"] * 4
    tech = -signals["rates"] if "rates" in signals else 0
    gold = signals["war"] * 2 + signals["inflation"] * 2
    vol = signals["volatility"] * 3 + signals["war"] * 1

    return {
        "EnergySector": energy,
        "DefenseSector": defense,
        "TechSector": tech,
        "GoldReaction": gold,
        "VolatilitySpike": vol
    }


# -----------------------------
# MAIN
# -----------------------------

def main():

    if len(sys.argv) < 2:
        print("Usage: python macro_ai_terminal_pro2.py image.png")
        sys.exit()

    image_path = sys.argv[1]

    print("\n=================================")
    print("GLOBAL MACRO AI TERMINAL PRO")
    print("=================================\n")

    raw_text = run_ocr(image_path)

    text = clean_text(raw_text)

    print("\nOCR TEXT DETECTED\n")
    print(raw_text[:1200])

    signals = detect_macro(text)

    df = pd.DataFrame.from_dict(signals, orient='index', columns=["Value"])

    print("\n\nMARKET DATA\n")
    print(df)

    regime = macro_regime(signals)

    print("\nMACRO REGIME\n")
    print(">>>", regime)

    sectors = sector_forecast(signals)

    print("\nSECTOR FORECAST\n")

    for k,v in sectors.items():
        print(k,"->",v,"%")

    print("\n=================================\n")


if __name__ == "__main__":
    main()
