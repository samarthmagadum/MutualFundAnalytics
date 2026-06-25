# Mutual Fund Analytics Data Dictionary

## 01_fund_master

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Asset Management Company |
| scheme_name | Text | Fund Scheme Name |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |
| plan | Text | Direct/Regular Plan |
| launch_date | Date | Scheme Launch Date |
| benchmark | Text | Benchmark Index |
| expense_ratio_pct | Float | Expense Ratio Percentage |
| exit_load_pct | Float | Exit Load Percentage |
| min_sip_amount | Integer | Minimum SIP Amount |
| min_lumpsum_amount | Integer | Minimum Lump Sum Amount |
| fund_manager | Text | Fund Manager Name |
| risk_category | Text | Risk Category |
| sebi_category_code | Text | SEBI Category Code |

---

## 02_nav_history

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## 07_scheme_performance

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund Code |
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| return_5yr_pct | Float | 5 Year Return |
| expense_ratio_pct | Float | Expense Ratio |
| sharpe_ratio | Float | Risk Adjusted Return |
| risk_grade | Text | Risk Rating |

---

## 08_investor_transactions

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | Integer | Investor ID |
| transaction_date | Date | Transaction Date |
| amfi_code | Integer | Fund Code |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| kyc_status | Text | KYC Status |