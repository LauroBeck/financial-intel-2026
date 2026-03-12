import cv2
import pytesseract
import pandas as pd
import re
import sys
import os

print("\n=================================")
print("GLOBAL MACRO AI TERMINAL PRO")
print("=================================\n")


# -----------------------------
# SCREEN READER
# -----------------------------

class ScreenReader:

    def read(self, path):

        if not os.path.exists(path):
            print("❌ File not found:", path)
            sys.exit()

        img = cv2.imread(path)

        if img is None:
            print("❌ Could not read image")
            sys.exit()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # improve OCR detection
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        gray = cv2.GaussianBlur(gray, (3,3), 0)

        # threshold improves text extraction
        gray = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        text = pytesseract.image_to_string(gray)

        return text


# -----------------------------
# BLOOMBERG PARSER
# -----------------------------

class BloombergParser:

    def parse(self, text):

        data = {}

        text = text.upper()

        # DEBUG (optional)
        print("\nOCR TEXT DETECTED\n")
        print(text)


        # -----------------
        # FIND ALL NUMBERS
        # -----------------

        numbers = re.findall(r'-?\d+\.\d+', text)

        numbers = [float(n) for n in numbers]


        # crude prices usually > 80
        oil_candidates = [n for n in numbers if 80 < n < 200]

        if oil_candidates:

            data["BRENT_PRICE"] = max(oil_candidates)


        # oil move (largest + number under 30)
        oil_moves = [n for n in numbers if 5 < n < 30]

        if oil_moves:

            data["OIL_MOVE"] = max(oil_moves)


        # futures (negative small numbers)
        futures = [n for n in numbers if -5 < n < 5]

        if len(futures) >= 3:

            data["SP500_FUT"] = futures[0]
            data["NASDAQ_FUT"] = futures[1]
            data["DAX_FUT"] = futures[2]


        # geopolitics
        data["WAR"] = ("WAR" in text) or ("IRAN" in text)

        return data


# -----------------------------
# MACRO ENGINE
# -----------------------------

class MacroEngine:

    def compute(self, data):

        oil = data.get("OIL_MOVE",0)
        sp = data.get("SP500_FUT",0)
        nasdaq = data.get("NASDAQ_FUT",0)
        war = data.get("WAR",False)

        regime = "NEUTRAL"

        if oil > 10 and war:
            regime = "GEOPOLITICAL OIL SHOCK"

        elif sp < -1:
            regime = "RISK OFF"

        elif sp > 1:
            regime = "RISK ON"


        energy = oil * 0.4
        defense = oil * 0.25 + (1 if war else 0)
        tech = nasdaq * 1.1
        gold = oil * 0.15
        volatility = abs(sp) * 2

        forecast = {

            "EnergySector": round(energy,2),
            "DefenseSector": round(defense,2),
            "TechSector": round(tech,2),
            "GoldReaction": round(gold,2),
            "VolatilitySpike": round(volatility,2)

        }

        return regime, forecast


# -----------------------------
# TERMINAL DISPLAY
# -----------------------------

class Terminal:

    def show(self, market, regime, forecast):

        print("\nMARKET DATA\n")

        if market:
            print(pd.DataFrame.from_dict(market, orient="index", columns=["Value"]))
        else:
            print("⚠ No values detected")

        print("\nMACRO REGIME\n")

        print(">>>", regime)

        print("\nSECTOR FORECAST\n")

        for k,v in forecast.items():

            print(k,"->",v,"%")


# -----------------------------
# MAIN
# -----------------------------

def main():

    if len(sys.argv) < 2:

        print("Usage:")
        print("python macro_ai_terminal_pro2.py screenshot.png")
        return


    image = sys.argv[1]

    reader = ScreenReader()

    text = reader.read(image)

    parser = BloombergParser()

    market = parser.parse(text)

    engine = MacroEngine()

    regime, forecast = engine.compute(market)

    terminal = Terminal()

    terminal.show(market, regime, forecast)


if __name__ == "__main__":
    main()

print("\n=================================\n")
