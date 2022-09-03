from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class User(UserBase):
    firstName: str
    lastName: str
    username: str
    email: str
    password: str