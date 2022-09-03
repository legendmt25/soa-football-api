from typing import Optional
from fastapi import APIRouter, Depends, Header
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.services import BettingService
from src.integrations import UserClient


router = APIRouter("/api")

@router.get('/bet')
@inject
def bet(
    userClient: UserClient = Depends(Provide[Container.userClient]),
    bettingService: BettingService = Depends(Provide[Container.bettingService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, [])
    return bettingService.placeBet('')