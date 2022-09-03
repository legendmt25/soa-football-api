from sqlalchemy import Column, Enum, Integer, Date, Numeric, String
from src.database import Base
from src.enums import TransactionStatus

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column("id", Integer, primary_key = True, index = True)
    userId = Column(String(50))
    createdAt = Column(Date)
    price = Column(Numeric)
    status = Column(Enum(TransactionStatus))