-- Top 5 funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Total SIP Amount
SELECT SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type='SIP';

-- Transactions By State
SELECT state,
COUNT(*)
FROM 08_investor_transactions
GROUP BY state;

-- Expense Ratio Below 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top 10 NAV
SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 10;

-- Average 1 Year Return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- Fund Count By Category
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- Risk Grade Distribution
SELECT risk_grade,
COUNT(*)
FROM 07_scheme_performance
GROUP BY risk_grade;

-- Top Fund Houses
SELECT fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;