# API routes for data ingestion and retrieval
from fastapi import APIRouter, BackgroundTasks, HTTPException
from src.app.models import DataPoint
from src.app.data_pipeline import ingest_data, process_data, data_collection, start_data_generation

router = APIRouter()

@router.post("/data/insert-new-data")
async def ingest_and_process_data_endpoint(data: DataPoint):
  await ingest_data(data)
  processed_data = await process_data()
  return {"message": "Data ingested and processed successfully", "data": data, "processed_data": processed_data}

@router.post("/data/processing")
async def process_data_endpoint():
  processed_data = await process_data()
  return {"message": "Data ingested and processed successfully", "processed_data": processed_data}

@router.get("/data/latest")
async def get_latest_data():
  if data_collection:
    return data_collection[-1]  # Return the latest data point
  else:
    raise HTTPException(status_code=404, detail="No data available")

@router.get("/data")
async def query_data(start: str = None, end: str = None):
  #TODO: Optionally, you can implement filtering based on start and end timestamps
  #INFO: For now, just return all data for simplicity
  return data_collection

@router.post("/start-data-load")
async def start_data_load(background_tasks: BackgroundTasks):
    """Endpoint to trigger data generation."""
    background_tasks.add_task(start_data_generation)
    return {"message": "Data generation has started."}