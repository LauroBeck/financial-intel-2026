import cv2
import pytesseract
import re


class BloombergScreenParser:

    def extract_text(self, image_path):

        img = cv2.imread(image_path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray)

        return text


    def parse_market_data(self, text):

        data = {}

        sp = re.search(r'S&P\s?500.*?(-?\d+\.\d+%)', text)

        if sp:
            data["SP500"] = float(sp.group(1).replace("%",""))

        nasdaq = re.search(r'NASDAQ.*?(-?\d+\.\d+%)', text)

        if nasdaq:
            data["NASDAQ"] = float(nasdaq.group(1).replace("%",""))

        vix = re.search(r'VIX.*?(-?\d+\.\d+%)', text)

        if vix:
            data["VIX"] = float(vix.group(1).replace("%",""))

        oil = re.search(r'BRENT.*?(-?\d+\.\d+%)', text)

        if oil:
            data["BRENT"] = float(oil.group(1).replace("%",""))

        return data
