from pydantic import BaseModel
from typing import Dict
from decimal import Decimal

class Weights(BaseModel):
    weights: Dict[str, Decimal]