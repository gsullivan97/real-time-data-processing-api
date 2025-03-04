#INFO: Main entry point for the FastAPI application
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routers.data_router import router as data_router

# import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
  # asyncio.create_task(generate_data())

  yield
  print("Shutting down the application...")

app = FastAPI(lifespan=lifespan)
app.include_router(data_router)
