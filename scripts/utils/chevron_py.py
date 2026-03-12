import pandas as pd
import numpy as np

# Brent futures from Bloomberg screen
data = {
    "Contract": ["May26", "Jun26", "Jul26", "Aug26"],
    "BrentPrice": [107.00, 99.32, 92.81, 88.06],
    "ChangePct": [15.44, 13.90, 11.98, 10.27]
}

df = pd.DataFrame(data)

# average oil shock
oil_shock = df["ChangePct"].mean()

print("Average Brent Shock:", round(oil_shock,2), "%")

# sensitivity coefficients
beta = {
    "Chevron": 0.65,
    "ExxonMobil": 0.60,
    "Halliburton": 0.85,
    "BakerHughes": 0.80,
    "BP": 0.58
}

results = {}

for company, sensitivity in beta.items():
    gain = oil_shock * sensitivity
    results[company] = round(gain,2)

energy_df = pd.DataFrame.from_dict(results, orient="index", columns=["ProjectedGain%"])

print("\nProjected Energy Sector Gains\n")
print(energy_df)
