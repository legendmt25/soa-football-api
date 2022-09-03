from http.client import responses
from typing import Optional
from fastapi import HTTPException
import requests


class PaymentClient:
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
    
    def pay(self, price: float, userId: int):
        try:
            response = requests.post(self.endpoint + 'api/pay', data={
                'price': price,
                'userId': userId
            })
            if not response.ok:
                raise HTTPException(408, 'Server error')
        except:
            raise HTTPException(408, "Cannot reach " + self.endpoint)
        return response.json()

class FootballClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

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

    def authenticate(self, Authorization: Optional[str], roles: list):
        if(len(roles) != 0 and Authorization == None):
            raise HTTPException(401, "You need to authenticate first")
        for role in roles:
            if(not self.userContainsRole(Authorization, role)):
                raise HTTPException(403, "Forbidden access to this endpoint")