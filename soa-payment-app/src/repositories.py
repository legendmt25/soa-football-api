from contextlib import AbstractContextManager
from datetime import date
from typing import Callable
from sqlalchemy.orm import Session

from src.schemas import Transaction

class TransactionRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
    
    def findAll(self):
        with self.session_factory() as db:
            return db.query(Transaction).all()

    def findById(self, transactionId: int):
        with self.session_factory() as db:
            return db.query(Transaction).filter(Transaction.id == transactionId).first()

    def findAllByCreatedAt(self, createdAt: date):
        with self.session_factory() as db:
            return db.query(Transaction).filter(Transaction.createdAt == createdAt).all()

    def findByUserId(self, userId: int):
        with self.session_factory() as db:
            return db.query(Transaction).filter(Transaction.userId == userId).all()
            
    def create(self, tx: any):
        with self.session_factory() as db:
            db.add(tx)
            db.commit()
            db.refresh(tx)
            return tx
        
    def update(self, tx: any):
        with self.session_factory() as db:
            db.add(tx)
            db.commit()
            db.refresh(tx)
            return tx