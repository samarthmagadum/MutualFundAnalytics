import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# ==========================
# 1. NAV HISTORY CLEANING
# ==========================

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav['date'] = pd.to_datetime(nav['date'])

nav = nav.sort_values(
    ['amfi_code', 'date']
)

nav['nav'] = nav.groupby(
    'amfi_code'
)['nav'].ffill()

nav = nav.drop_duplicates()

nav = nav[nav['nav'] > 0]

nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned")

# ==========================
# 2. INVESTOR TRANSACTIONS
# ==========================

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn['transaction_date'] = pd.to_datetime(
    txn['transaction_date']
)

txn['transaction_type'] = (
    txn['transaction_type']
    .str.upper()
    .str.strip()
)

txn = txn[
    txn['amount_inr'] > 0
]

valid_kyc = [
    'VERIFIED',
    'PENDING',
    'REJECTED'
]

txn['kyc_status'] = (
    txn['kyc_status']
    .str.upper()
)

txn = txn[
    txn['kyc_status'].isin(valid_kyc)
]

txn.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Transactions Cleaned")

# ==========================
# 3. SCHEME PERFORMANCE
# ==========================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct'
]

for col in return_cols:

    perf[col] = pd.to_numeric(
        perf[col],
        errors='coerce'
    )

anomalies = perf[
    (perf['expense_ratio_pct'] < 0.1)
    |
    (perf['expense_ratio_pct'] > 2.5)
]

print("\nExpense Ratio Anomalies")
print(anomalies.shape)

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Performance Cleaned")

other_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in other_files:

    df = pd.read_csv(
        "data/raw/" + file
    )

    df = df.drop_duplicates()

    df = df.dropna(how='all')

    output = (
        "data/processed/"
        + file.replace(".csv", "_clean.csv")
    )

    df.to_csv(
        output,
        index=False
    )

    print(file, "Cleaned")