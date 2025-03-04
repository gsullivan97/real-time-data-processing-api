# Script for simulating real-time data generation
import asyncio
import random
from datetime import datetime
from src.app.models import DataPoint

async def generate_data(data_collection):
  while True:
    data = DataPoint(
      timestamp=datetime.now().isoformat(),
      id=random.randint(1, 100),
      value=random.uniform(1.0, 100.0)
    )

    data_collection.append(data)

    #INFO: debugging the generated data
    print("Generated Data:", data.model_dump_json())

    # INFO: add a delay to avoid overwhelming the server
    await asyncio.sleep(1)