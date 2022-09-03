from datetime import date
from typing import Iterable

from src.enums import TransactionStatus
from src.repositories import TransactionRepository

from src.models import DailyReport, TransactionCreate
from src.schemas import Transaction
import src.models as models

class TransactionService:
    def __init__(self, transactionRepository: TransactionRepository):
        self.transactionRepository = transactionRepository
    
    def findAll(self) -> Iterable[models.Transaction]:
        return self.transactionRepository.findAll()

    def findById(self, id: int) -> models.Transaction:
        return self.transactionRepository.findById(id)

    def findAllByCreatedAt(self, createdAt: date) -> Iterable[models.Transaction]:
        return self.transactionRepository.findAllByCreatedAt(createdAt)

    def findAllByUserId(self, userId: int) -> Iterable[models.Transaction]:
        return self.transactionRepository.findByUserId(userId)

    def pay(self, tx: any):
        self.create(tx)
        return 200

    def create(self, tx: TransactionCreate) -> models.Transaction:
        return self.transactionRepository.create(
            Transaction(
                userId = tx.userId, 
                createdAt = date.today(), 
                price = tx.price, 
                status = TransactionStatus.PENDING,
            )
        )

    def setTransactionStatus(self, id: int, status: TransactionStatus) -> bool:
        transaction = self.findById(id)
        transaction.status = status
        self.transactionRepository.update(transaction)
        return True

    def cancelTransaction(self, id: int) -> bool:
        self.setStatus(id, TransactionStatus.CANCELED)
        return True

    def getDailyReportForDate(self, date: date) -> DailyReport:
        txs = self.findAllByCreatedAt(date)
        return DailyReport(
            date = date, 
            totalTransactions = len(txs), 
            totalPending = len(list(filter(lambda x: x.status == TransactionStatus.PENDING, txs))), 
            totalResolved = len(list(filter(lambda x: x.status == TransactionStatus.RESOLVED, txs))), 
            totalCanceled = len(list(filter(lambda x: x.status == TransactionStatus.CANCELED, txs))), 
            totalPrice = sum(map(lambda x: x.price, txs))
        )