from fastapi import APIRouter, Header, Depends
from dependency_injector.wiring import inject, Provide

from src.services import UserService
from src.containers import Container
from src.models import User

router = APIRouter(prefix='/api')

@router.post("/register")
@inject
def register(data: User, userService: UserService = Depends(Provide[Container.userService])):
   return userService.register(data)

@router.get('/token')
@inject
def userInfo(x_token = Header(), userService: UserService = Depends(Provide[Container.userService])):
    return userService.userInfo(x_token)

@router.get('/users')
@inject
def users(userService: UserService = Depends(Provide[Container.userService])):
    return userService.keycloakAdmin.get_users()