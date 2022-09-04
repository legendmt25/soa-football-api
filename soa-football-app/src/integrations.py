from typing import Optional
from fastapi import HTTPException
import requests

from src.enums import OddsType


class FootballClient:
    def __init__(self, endpoint: str, apiKey: str):
        self.endpoint = endpoint
        self.apiKey = apiKey
        self.headers = { 'apikey': apiKey, 'content-type': 'application/json' }

    def findAllMatches(self, season_id: int):
        params=(
            ('season_id', season_id),
        )
        res = requests.get(self.endpoint + 'matches', headers=self.headers, params=params)
        return res.json()['data']

    def findAllLiveMatches(self):
        params = (
            ('live', True),
        )
        res = requests.get(self.endpoint + 'matches', headers=self.headers, params=params)
        return res.json()['data']

    def findAllLiveMatchesBySeasonId(self, seasonId: int):
        params = (
            ('live', True),
            ('season_id', seasonId),
        )
        res = requests.get(self.endpoint + 'matches', headers=self.headers, params=params)
        return res.json()['data']
    
    def findMatchById(self, id: int):
        res = requests.get(self.endpoint + 'matches/' + str(id), headers=self.headers)
        return res.json()['data']
        
    def findAllLeagues(self):
        res = requests.get(self.endpoint + 'leagues', headers=self.headers)
        return res.json()['data']

    def findAllLeaguesByCountry(self, country_id: int):
        params = (
            ('country_id', country_id),
        )
        res = requests.get(self.endpoint + 'leagues', headers=self.headers, params=params)
        return res.json()['data']

    def findLeagueById(self, id: int):
        res = requests.get(self.endpoint + 'leagues/' + str(id), headers=self.headers)
        return res.json()['data']

    def findAllSeasons(self, league_id: int):
        params = (
            ('league_id', league_id),
        )
        res = requests.get(self.endpoint + 'seasons', headers=self.headers, params=params)
        return res.json()['data']

    def findSeasonById(self, id: int, league_id: int):
        params = (
            ('league_id', league_id),
        )
        res = requests.get(self.endpoint + 'seasons/' + str(id), headers=self.headers, params=params)
        return res.json()['data']

    def findAllVenuse(self, country_id: int):
        params = (
            ('country_id', country_id),
        )
        res = requests.get(self.endpoint + 'venues', headers=self.headers, params=params)
        return res.json()['data']

    def findVenueById(self, id: int, country_id: int):
        params = (
            ('country_id', country_id),
        )
        res = requests.get(self.endpoint + 'seasons/' + str(id), headers=self.headers, params=params)
        return res.json()['data']

    def findOddsByMatch(self, match_id: int, oddsType: OddsType):
        params = (
            ('type', oddsType.value),
        )
        res = requests.get(self.endpoint + 'odds/' + str(match_id), headers=self.headers, params=params)
        return res.json()['data']

class UserClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
    
    def userContainsRole(self, jwttoken: str, roleName: str) -> bool:
        try:
            response = requests.get(self.endpoint + "userContainsRole", data={ "roleName": roleName }, headers={ "Authorization": jwttoken })
        except:
            raise HTTPException(408, "Cannot reach " + self.endpoint)
        hasAccess = response.json()
        return hasAccess
    
    def getUserId(self, jwttoken: str) -> str:
        try:
            response = requests.get(self.endpoint + "user/info", headers={ "Authorization": jwttoken })
        except:
            raise HTTPException(408, "Cannot reach " + self.endpoint)
        user = response.json()
        return user['username']

    def authorize(self, Authorization: Optional[str], roles: list):
        if(len(roles) != 0 and Authorization == None):
            raise HTTPException(401, "You need to authenticate first")
        for role in roles:
            if(not self.userContainsRole(Authorization, role)):
                raise HTTPException(403, "Forbidden access to this endpoint")