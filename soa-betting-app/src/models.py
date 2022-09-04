from datetime import date
from pydantic import BaseModel

class BetMatchBase(BaseModel): 
    matchId: int
    playType: str


class BetMatchCreate(BetMatchBase):
    pass

class BetMatch(BetMatchBase):
    id: int

    class Config:
        orm_mode = True



class BetBase(BaseModel):
    price: float

class BetCreate(BetBase):
    matches: list[BetMatchCreate]

class Bet(BetBase):
    id: int
    userId: int
    matches: list[BetMatch]
    createdAt: date
        
    class Config:
        orm_mode = True

