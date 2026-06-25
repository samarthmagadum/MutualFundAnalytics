import pandas as pd
import os

from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

folder = "data/processed"

files = [
    f for f in os.listdir(folder)
    if f.endswith(".csv")
]

for file in files:

    table_name = (
        file.replace(
            "_clean.csv",
            ""
        )
    )

    df = pd.read_csv(
        os.path.join(
            folder,
            file
        )
    )

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        table_name,
        "loaded"
    )

print("Database Created")