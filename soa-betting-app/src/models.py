from datetime import date
from pydantic import BaseModel

class BetBase(BaseModel):
    pass

class BetCreate(BetBase):
    userId: str

class Bet(BetBase):
    id: int
    userId: str
    createdAt: date
    price: float

    class Config:
        orm_mode = True