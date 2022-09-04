from sys import prefix
from typing import Optional
from fastapi import APIRouter, Depends, Header
from dependency_injector.wiring import inject, Provide
from src.enums import OddsType

from src.containers import Container
from src.services import FootballService
from src.integrations import UserClient


router = APIRouter(prefix='/api')

@router.get('/matches')
@inject
def matches(
    season_id: Optional[int] = None,
    live: Optional[bool] = None,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, [])
    return footballService.findAllMatches(season_id, live)

@router.get('/matches/{id}')
@inject
def match(
    id: int,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, [])
    print(id)
    return footballService.findMatchById(id)


@router.get('/leagues')
@inject
def leagues(
    country_id: Optional[int] = None,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, [])
    return footballService.findAllLeagues(country_id)

@router.get('/leagues/{id}')
@inject
def league(
    id: int,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, [])
    return footballService.findMatchById(id)

@router.get('/seasons')
@inject
def seasons(
    league_id: int,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, [])
    return footballService.findAllSeasons(league_id)

@router.get('/odds/{match_id}')
@inject
def odds(
    match_id: int,
    oddsType: OddsType,
    userClient: UserClient = Depends(Provide[Container.userClient]),
    footballService: FootballService = Depends(Provide[Container.footballService]),
    Authorization: Optional[str] = Header(None)
):
    userClient.authorize(Authorization, [])
    return footballService.findOddsByMatchId(match_id, oddsType)
