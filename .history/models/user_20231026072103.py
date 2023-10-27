
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from models.pyObjectId import *



class UserInDB(BaseModel):
    id: PyObjectId = Field(alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    fullName: str = Field(...)
    phone: str = Field(...)
    address: str = Field(...)
    createdAt: str = Field(...)

class UserRegister(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    fullName: str = Field(...)
    phone: str = Field(...)
    address: str = Field(...)

class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
   
class UserModel(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    
    
class UpdateUserModel(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    
    
class UserUpdateRequest(BaseModel):
    full_name: str = None
    address: str = None
    username: str = None