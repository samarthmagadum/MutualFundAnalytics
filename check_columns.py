import pandas as pd

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv"
]

for file in files:

    print("\n" + "="*60)
    print(file)

    df = pd.read_csv("data/raw/" + file)

    print(df.columns.tolist())