from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Header, status
from dependency_injector.wiring import inject, Provide
from src.enums import OddsType

from src.containers import Container
from src.services import FootballService
from src.integrations import UserClient


router = APIRouter()


def authorize(userClient: UserClient, authorization: Optional[str], roles: list[str]):
    if(len(roles) != 0 and authorization == None):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "You need to authenticate first")

    for role in roles:
        if not userClient.userContainsRole(authorization, role):
            raise HTTPException(status.HTTP_403_FORBIDDEN,
                                "Forbidden access to this endpoint")
    return True

@router.get('/api/v1/matches')
@inject
def matches(
    season_id: Optional[int] = None,
    live: Optional[bool] = None,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    authorize(userClient, Authorization, [])
    return footballService.findAllMatches(season_id, live)

@router.get('/api/v1/matches/:id')
@inject
def match(
    id: int,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    authorize(userClient, Authorization, [])
    return footballService.findMatchById(id)


@router.get('/api/v1/leagues')
@inject
def leagues(
    country_id: Optional[int] = None,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    authorize(userClient, Authorization, [])
    return footballService.findAllLeagues(country_id)

@router.get('/api/v1/leagues/:id')
@inject
def league(
    id: int,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    authorize(userClient, Authorization, [])
    return footballService.findMatchById(id)

@router.get('/api/v1/seasons')
@inject
def seasons(
    league_id: int,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    authorize(userClient, Authorization, [])
    return footballService.findAllSeasons(league_id)

@router.get('/api/v1/odds/:match_id')
@inject
def odds(
    match_id: int,
    type: OddsType,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    authorize(userClient, Authorization, [])
    return footballService.findOddsByMatchId(match_id, type)
