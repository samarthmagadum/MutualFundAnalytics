import requests
import pandas as pd

funds = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for fund_name, code in funds.items():

    print("Fetching:", fund_name)

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    file_name = f"data/raw/{fund_name}.csv"

    df.to_csv(file_name, index=False)

    print("Saved:", file_name)