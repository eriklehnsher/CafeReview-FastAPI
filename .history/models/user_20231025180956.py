
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from models.pyObjectId import *



class UserInDB(BaseModel):
    id:  str Field(...)
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)

class UserRegister(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
   
class UserModel(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)