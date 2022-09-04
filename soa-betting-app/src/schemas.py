from sqlalchemy import Column, Integer, Date, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Bet(Base):
    __tablename__ = "bets"

    id = Column("id", Integer, primary_key = True, index = True)
    userId = Column(Integer)
    createdAt = Column(Date)
    price = Column(Numeric)
    matches = relationship("BetMatch", lazy='joined')
    

class BetMatch(Base):
    __tablename__ = "bet_matches"
    
    id = Column("id", Integer, primary_key = True, index = True)
    matchId = Column(Integer)
    playType = Column(String)
    bet_id = Column(Integer, ForeignKey("bets.id"))