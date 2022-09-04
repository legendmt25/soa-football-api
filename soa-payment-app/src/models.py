from datetime import date
from pydantic import BaseModel

from src.enums import TransactionStatus

class TransactionBase(BaseModel):
    price: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    type: str
    userId: str
    createdAt: date
    status: TransactionStatus
    class Config:
        orm_mode = True

class DailyReport(BaseModel):
    date: date
    totalTransactions: int
    totalResolved: int
    totalPending: int
    totalCanceled: int
    totalPrice: float