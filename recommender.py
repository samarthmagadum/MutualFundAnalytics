# Import pandas

import pandas as pd

# Read cleaned scheme performance dataset

scheme = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

# Ask user for risk level

risk = input(
    "Enter Risk Level (Low / Moderate / High): "
)

# Filter matching funds

result = scheme[
    scheme["risk_grade"] == risk
]

# Sort by Sharpe Ratio

result = result.sort_values(
    by="sharpe_ratio",
    ascending=False
)

# Display Top 3 funds

print("\nTop Recommended Funds\n")

print(
    result[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio"
        ]
    ].head(3)
)