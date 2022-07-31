from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Header, status
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.models import Fixtures
from src.services import FootballService
from src.integrations import UserClient


router = APIRouter()


def authorize(userClient: UserClient, authorization: Optional[str], roles: list[str]):
    if(authorization == None):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "You need to authenticate first")

    for role in roles:
        if not userClient.userContainsRole(authorization, role):
            raise HTTPException(status.HTTP_403_FORBIDDEN,
                                "Forbidden access to this endpoint")
    return True

@router.get('/api/v1/fixtures')
@inject
def fixtures(
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.FootballService]),
    Authorization: Optional[str] = Header(None)
) -> list[Fixtures]:
    authorize(userClient, Authorization, [])
    return footballService.findAllFixtures()
