# Pydantic models for data validation
from pydantic import BaseModel

class DataPoint(BaseModel):
  timestamp: str
  id: int
  value: float