import asyncio
import json
from fastapi.responses import JSONResponse
from src.app.models import DataPoint
from src.services.data_processing import transform_data, analyze_data
from src.app.data_generator import generate_data

data_collection = []

async def start_data_generation():
  """Start generating data in the background."""
  await generate_data(data_collection)

async def ingest_data(data: DataPoint):
  data_collection.append(data)

async def process_data():
  if data_collection:
    df = transform_data(data_collection)
    analyzed_df = analyze_data(df)

    print("Processed Data:\n", analyzed_df)
    analyzed_df.index = analyzed_df.index.astype(str)
    analyzed_df.fillna('NaN', inplace=True)
    json_data = analyzed_df.reset_index().to_dict(orient='records')

    # INFO: Save the processed data to a JSON file
    with open('test.json', 'w') as json_file:
      json.dump(json_data, json_file, indent=2)

    return json_data