from sqlalchemy import Column, Integer, String, Date, Numeric
from src.database import Base

class Bet(Base):
    __tablename__ = "bets"

    id = Column("id", Integer, primary_key = True, index = True)
    userId = Column(String(50))
    createdAt = Column(Date)
    price = Column(Numeric)