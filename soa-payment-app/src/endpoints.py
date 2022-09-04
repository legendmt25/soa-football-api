from datetime import date
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Header
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.models import TransactionCreate
from src.enums import TransactionStatus
from src.services import TransactionService
from src.integrations import UserClient


router = APIRouter(prefix='/api')

@router.post('/pay')
@inject
def pay(
    body: TransactionCreate,
    Authorization: Optional[str] = Header(None),
    userClient: UserClient = Depends(Provide[Container.userClient]),
    transactionService: TransactionService = Depends(Provide[Container.transactionService])
):
    userClient.authorize(Authorization, ["Client", "Employee", "Admin"])    
    userId = userClient.getUserId(Authorization)
    return transactionService.pay(
        TransactionCreate(
            price=body.price, 
            userId=userId
        )
    )
        
@router.get('/transactions')
@inject
def transactions(
    Authorization: Optional[str] = Header(None),
    userClient: UserClient = Depends(Provide[Container.userClient]),
    transactionService: TransactionService = Depends(Provide[Container.transactionService])
):
    userClient.authorize(Authorization, ["Employee", "Admin"])
    return transactionService.findAll()

@router.post("/transactions-by-creation")
@inject
def transactionsByCreatedAt(
    date: date,
    Authorization: Optional[str] = Header(None),
    userClient: UserClient = Depends(Provide[Container.userClient]),
    transactionService: TransactionService = Depends(Provide[Container.transactionService])
):
    userClient.authorize(Authorization, ["Employee", "Admin"])
    return transactionService.findAllByCreatedAt(date)

@router.post("/transactions-by-userid")
@inject
def transactionsByUserId(
    userId: int,
    Authorization: Optional[str] = Header(None),
    userClient: UserClient = Depends(Provide[Container.userClient]),
    transactionService: TransactionService = Depends(Provide[Container.transactionService])
):
    userClient.authorize(Authorization, ["Employee", "Admin"])
    return transactionService.findAllByUserId(userId)

@router.get("/transaction/{id}")
@inject
def transaction(
    id: int,
    Authorization: Optional[str] = Header(None),
    userClient: UserClient = Depends(Provide[Container.userClient]),
    transactionService: TransactionService = Depends(Provide[Container.transactionService])
):
    userClient.authorize(Authorization, ["Employee", "Admin"])
    return transactionService.findById(id)

@router.post("/transaction/create")
@inject
def create(
    transaction: TransactionCreate,
    Authorization: Optional[str] = Header(None),
    userClient: UserClient = Depends(Provide[Container.userClient]),
    transactionService: TransactionService = Depends(Provide[Container.transactionService])
):
    userClient.authorize(Authorization, ["Employee", "Admin"])
    return transactionService.create(transaction)
    
@router.post("/transaction/{id}/set-status")
@inject
def setStatus(
    id: int, 
    status: TransactionStatus,
    Authorization: Optional[str] = Header(None),
    userClient: UserClient = Depends(Provide[Container.userClient]),
    transactionService: TransactionService = Depends(Provide[Container.transactionService])
):
    userClient.authorize(Authorization, ["Admin"])
    return transactionService.setTransactionStatus(id, status)

@router.get("/daily-report")
@inject
def getDailyReport(
    date: date,
    Authorization: Optional[str] = Header(None),
    userClient: UserClient = Depends(Provide[Container.userClient]),
    transactionService: TransactionService = Depends(Provide[Container.transactionService])
):
    userClient.authorize(Authorization, ["Admin"])    
    return transactionService.getDailyReportForDate(date)