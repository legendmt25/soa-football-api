from datetime import date
from pydantic import BaseModel

from src.enums import TransactionStatus

class TransactionBase(BaseModel):
    price: float

class TransactionCreatePartial(TransactionBase):
    pass

class TransactionCreate(TransactionCreatePartial):
    userId: str

class Transaction(TransactionBase):
    id: int
    type: str
    userId: str
    createdAt: date
    status: TransactionStatus
    class Config:
        orm_mode = True

class MarketTransaction(Transaction):
    shoppingCartId: int
    class Config:
        orm_mode = True

class ServiceTransaction(Transaction):
    petId: int
    serviceIds: list
    class Config:
        orm_mode = True

class ResourceTransaction(Transaction):
    petId: int
    resourceIds: list
    class Config:
        orm_mode = True

class DailyReport(BaseModel):
    date: date
    totalTransactions: int
    totalResolved: int
    totalPending: int
    totalCanceled: int
    totalPrice: float