#INFO: Main entry point for the FastAPI application
from fastapi import FastAPI
from src.routers.data_router import router as data_router
from src.app.data_generator import generate_data
import asyncio

app = FastAPI()

app.include_router(data_router)

@app.on_event("startup")
async def startup_event():
  print("Starting data generation")
  asyncio.create_task(generate_data())