import pandas as pd
from sqlalchemy import create_engine


def create_database(csv_path="cleaned_ops.csv", db_path="operations.db"):
    """Create the SQLite database used by the Week 3 pipeline."""
    df_ops = pd.read_csv(csv_path, parse_dates=["timestamp"])
    df_ops["date"] = df_ops["timestamp"].dt.normalize()

    calendar = pd.DataFrame({
        "date": pd.date_range(
            df_ops["date"].min(),
            df_ops["date"].max(),
            freq="D"
        )
    })

    calendar["holiday_type"] = calendar["date"].dt.dayofweek.map(
        lambda day: "Weekend" if day >= 5 else "Working Day"
    )

    engine = create_engine(f"sqlite:///{db_path}")

    df_ops.to_sql("Operations", engine, if_exists="replace", index=False)
    calendar.to_sql("Holiday_Calendar", engine, if_exists="replace", index=False)

    print(f"Database created: {db_path}")
    print("Tables: Operations, Holiday_Calendar")


if __name__ == "__main__":
    create_database()
