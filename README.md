# Week 3: Multi-Source Operational Data Pipeline

## Objective
Integrate operational CSV data, a weather API, and a SQLite database into one master dataset for operational analysis.

## Data Sources
- Internal: cleaned_ops.csv
- External API: wttr.in Weather API
- Database: SQLite Holiday Calendar

## Technologies
- Python
- Pandas
- Requests
- SQLAlchemy
- SQLite
- Matplotlib

## Analysis
The integrated dataset was used to investigate the relationship between operational pressure and flow rate using Pearson correlation.

## Result
The correlation coefficient (-0.009) indicates almost no linear relationship between pressure and flow rate.