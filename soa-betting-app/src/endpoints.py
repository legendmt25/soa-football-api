from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Header, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.services import BettingService
from src.integrations import UserClient


router = APIRouter("/api")


def authorize(userClient: UserClient, authorization: Optional[str], roles: list[str]):
    if(len(roles) != 0 and authorization == None):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "You need to authenticate first")

    for role in roles:
        if not userClient.userContainsRole(authorization, role):
            raise HTTPException(status.HTTP_403_FORBIDDEN,
                                "Forbidden access to this endpoint")
    return True

@router.get('/bet')
@inject
def bet(
    userClient: UserClient = Depends(Provide[Container.userClient]),
    bettingService: BettingService = Depends(Provide[Container.bettingService]),
    Authorization: Optional[str] = Header(None)
):
    authorize(userClient, Authorization, [])
    return bettingService.placeBet('')