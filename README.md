# Week 3: Multi-Source Operational Data Pipeline

## Objective
Integrate internal operational data, external weather data, and a SQLite calendar into a single master DataFrame for operational analysis.

## Deliverables
- `week3_multi_source_pipeline.ipynb` - complete technical pipeline
- `cleaned_ops.csv` - internal operational dataset
- `fetch_weather.py` - external API ingestion with error handling
- `create_database.py` - SQLite database creation
- `operations.db` - SQLite database
- `Week3_LightningTalk_Sharon.pdf` - three-slide presentation
- `peer_review.txt` - peer code review template

## Data Sources

### Source 1: Internal
`cleaned_ops.csv` contains operational event measurements including timestamp, zone, shift, pressure, temperature and flow rate.

### Source 2: External API
Weather observations are retrieved from an external weather API at runtime. Because the internal operational records are historical, the notebook requests date-matched daily weather observations so the integration uses a common date key.

### Source 3: SQLite
`operations.db` contains:
- `Operations`
- `Holiday_Calendar`

The notebook uses SQL `JOIN` and `GROUP BY` and loads the result directly into a DataFrame with `pd.read_sql()`.

## Integration
The final `master_df` combines:
1. Event-level operational data from CSV.
2. Date-level SQL summaries and calendar classification.
3. Date-level weather API observations.

All three sources are aligned using the `date` key.

## Analysis
The primary analysis calculates the Pearson correlation between `Pressure_PSI` and `Flow_Rate_LPM`. The original analysis produced a coefficient of approximately `-0.009`, indicating an essentially negligible linear relationship.

A secondary weather check examines rainfall against daily average flow rate.

## Technologies
Python, Pandas, Requests, SQLAlchemy, SQLite and Matplotlib.
