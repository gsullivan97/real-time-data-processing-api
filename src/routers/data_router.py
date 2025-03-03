# API routes for data ingestion and retrieval
from fastapi import APIRouter
from src.app.models import DataPoint
from src.app.data_pipeline import ingest_data, process_data, data_collection

router = APIRouter()

@router.post("/data/")
async def ingest_data_endpoint(data: DataPoint):
  await ingest_data(data)
  processed_data = await process_data()  # Process data after ingestion
  return {"message": "Data ingested and processed successfully", "data": data, "processed_data": processed_data}

@router.get("/data/")
async def get_data():
  return {"data": data_collection}