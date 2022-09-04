from typing import Optional
import fastapi
from fastapi import APIRouter, Depends, Header, HTTPException
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.services import BettingService
from src.integrations import UserClient, PaymentClient
from src.models import BetCreate

router = APIRouter(prefix='/api')

@router.get('/bets')
@inject
def getBets(
    userClient: UserClient = Depends(Provide[Container.userClient]),
    bettingService: BettingService = Depends(Provide[Container.bettingService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, ['Employee', 'Admin'])
    return bettingService.findAll()

@router.get('/bet/{id}')
@inject
def getBet(
    id: int,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    bettingService: BettingService = Depends(Provide[Container.bettingService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, ['Employee', 'Admin'])
    return bettingService.findById(id)

@router.post('/bet')
@inject
def bet(
    bet: BetCreate,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    paymentClient: PaymentClient = Depends(Provide[Container.paymentClient]),
    bettingService: BettingService = Depends(Provide[Container.bettingService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, ['Employee', 'Admin', 'Client'])
    status = paymentClient.pay(bet.price, Authorization)
    if status != 200:
        raise HTTPException(408, 'Payment unsuccessfull')
    userId = userClient.getUserId(Authorization)
    return bettingService.placeBet(bet, userId)

@router.get('/print-bet/{id}')
@inject
def bet(
    id: int,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    bettingService: BettingService = Depends(Provide[Container.bettingService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, ['Employee', 'Admin'])

    return fastapi.responses.StreamingResponse(    
        bettingService.printTicket(id, Authorization), 
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={ "Content-Disposition": "attachment;filename=" + str(id) + ".docx" }
    )