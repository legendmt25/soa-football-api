from contextlib import AbstractContextManager
from datetime import date
from typing import Callable
from sqlalchemy.orm import Session

from src.schemas import Bet

class BettingRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
    
    def findAll(self):
        with self.session_factory() as db:
            return db.query(Bet).all()

    def findById(self, betId: int):
        with self.session_factory() as db:
            return db.query(Bet).filter(Bet.id == betId).first()

    def findAllByCreatedAt(self, createdAt: date):
        with self.session_factory() as db:
            return db.query(Bet).filter(Bet.createdAt == createdAt).all()

    def findByUserId(self, userId: int):
        with self.session_factory() as db:
            return db.query(Bet).filter(Bet.userId == userId).all()
            
    def create(self, bet: any):
        with self.session_factory() as db:
            db.add(bet)
            db.commit()
            db.refresh(bet)
            return bet
        
    def update(self, bet: any):
        with self.session_factory() as db:
            db.add(bet)
            db.commit()
            db.refresh(bet)
            return bet