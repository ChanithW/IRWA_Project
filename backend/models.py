from pydantic import BaseModel
from typing import List

class Cart(BaseModel):
    user_id: int
    cart_value: float
    items: List[str]

class OfferResponse(BaseModel):
    user_response: int  # 1 = accepted, 0 = ignored
