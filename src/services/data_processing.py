import pandas as pd
from typing import List
from src.app.models import DataPoint

def transform_data(data: List[DataPoint]) -> pd.DataFrame:
  """Transforms a list of DataPoint objects into a melted pandas DataFrame."""
  df = pd.DataFrame([data_point.model_dump() for data_point in data])

  #2. Data Processing: Example of transformation - Melt the DataFrame
  melted_df = df.melt(id_vars=['timestamp'], value_vars=['id', 'value'], var_name='variable', value_name='value_transformed')

  return melted_df

def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
  """Analyzes a pandas DataFrame by filtering and computing a moving average."""
  #2. Data Processing: Filter for the 'value_transformed' rows
  value_df = df[df['variable'] == 'value']

  if value_df.empty:
    print("No data found for value_transformed.")
    return value_df

  #2. Data Processing: Compute a moving average for the 'value_transformed' column
  value_df['moving_average'] = value_df['value_transformed'].rolling(window=3).mean()

  #2. Data Processing: Aggregating data over time
  value_df['timestamp'] = pd.to_datetime(value_df['timestamp'])
  value_df.set_index('timestamp', inplace=True)

  return value_df