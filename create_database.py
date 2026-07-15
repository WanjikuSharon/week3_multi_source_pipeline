import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///operations.db")

holiday_data = pd.DataFrame({
    "date": pd.to_datetime([
        "2026-06-25",
        "2026-06-26",
        "2026-06-27",
        "2026-06-28",
        "2026-06-29"
    ]),
    "holiday_type": [
        "Working Day",
        "Working Day",
        "Weekend",
        "Weekend",
        "Working Day"
    ]
})

holiday_data.to_sql(
    "Holiday_Calendar",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")