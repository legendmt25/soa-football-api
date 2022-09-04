from typing import Optional
from fastapi import HTTPException
import requests


class PaymentClient:
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
    
    def pay(self, price: float, jwttoken: str) -> int:
        try:
            response = requests.post(url=self.endpoint + 'api/pay', data={
                'price': price,
            }, headers={ 'Authorization': jwttoken })
            if not response.ok:
                raise HTTPException(408, 'Server error')
        except:
            raise HTTPException(408, "Cannot reach " + self.endpoint)
        return response.json()

class FootballClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def getMatchById(self, matchId: int, jwttoken: str):
        try:
            response = requests.get(url=self.endpoint + 'api/matches/' + str(matchId), headers={ 'Authorization': jwttoken })
            if not response.ok:
                raise HTTPException(408, 'Server error')
        except:
            raise HTTPException(408, "Cannot reach " + self.endpoint)
        return response.json()

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
        return True
        if(len(roles) != 0 and Authorization == None):
            raise HTTPException(401, "You need to authenticate first")
        for role in roles:
            if(not self.userContainsRole(Authorization, role)):
                raise HTTPException(403, "Forbidden access to this endpoint")