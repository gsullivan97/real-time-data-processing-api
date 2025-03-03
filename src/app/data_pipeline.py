import asyncio
from fastapi.responses import JSONResponse
from src.app.models import DataPoint
from src.services.data_processing import transform_data, analyze_data

data_collection = []

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

    return json_data