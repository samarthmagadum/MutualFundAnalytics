# Mutual Fund Analytics

A complete Mutual Fund Analytics project developed during the Bluestock Fintech Internship using Python, SQL, SQLite, and Power BI. The project analyzes mutual fund performance, investor behavior, portfolio risk, and market trends through interactive dashboards and financial analytics.


## Project Objectives

- Analyze mutual fund industry data using Python and SQL.
- Clean and preprocess financial datasets.
- Perform Exploratory Data Analysis (EDA).
- Calculate advanced performance metrics such as Sharpe Ratio, Sortino Ratio, Alpha, Beta, VaR, and CVaR.
- Build interactive Power BI dashboards.
- Develop a simple mutual fund recommendation system based on investor risk appetite.


## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- Jupyter Notebook
- Power BI
- Visual Studio Code
- Git & GitHub


## Project Structure

MutualFundAnalytics/
│
├── dashboard/
├── data/
├── notebooks/
├── presentation/
├── reports/
├── sql/
├── venv/
│
├── .gitignore
├── bluestock_mf.db
├── check_columns.py
├── clean_data.py
├── data_ingestion.py
├── live_nav_fetch.py
├── load_to_sqlite.py
├── README.md
├── recommender.py
├── requirements.txt


## Dataset

The project uses multiple datasets related to the Indian mutual fund industry, including:

- Fund Master Data
- NAV History
- Assets Under Management (AUM)
- Monthly SIP Inflows
- Category-wise Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices


## Features

- Data Cleaning and Validation
- SQLite Database Integration
- Exploratory Data Analysis (EDA)
- Financial Performance Analysis
- Risk Analysis (VaR, CVaR)
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Mutual Fund Recommendation System
- Interactive Power BI Dashboard


## Dashboard Pages

- Industry Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends
- Benchmark Performance


## Key Insights

- Equity funds generated higher long-term returns than debt funds.
- Larger AUM schemes attracted more investor inflows.
- Higher Sharpe Ratio funds offered better risk-adjusted returns.
- Most SIP investments were concentrated in equity categories.
- The recommendation system identifies suitable funds based on investor risk preference.


## How to Run

1. Clone the repository.
2. Install the required libraries:

pip install -r requirements.txt

3. Run the data preprocessing scripts.
4. Execute the Jupyter notebooks.
5. Open the Power BI dashboard (.pbix file).
6. Run recommender.py to get fund recommendations.


## Future Scope

- Live mutual fund data integration.
- Machine learning-based recommendation system.
- Portfolio optimization.
- Real-time dashboard updates.
- Mobile application development.


## Author

**Samarth Magadum**

Bluestock Fintech Internship

Year: 2026
