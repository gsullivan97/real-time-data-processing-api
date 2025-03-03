# API routes for data ingestion and retrieval
from fastapi import APIRouter
from src.app.models import DataPoint

router = APIRouter()
data_collection = []

@router.post("/data/")
async def ingest_data(data: DataPoint):
  data_collection.append(data)
  return {"message": "Data ingested successfully", "data": data}

@router.get("/data/")
async def get_data():
  return {"data": data_collection}