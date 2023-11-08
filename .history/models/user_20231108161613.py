
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from models.pyObjectId import *



class UserInDB(BaseModel):
   
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    createdAt: str = Field(...)
    fullName: str = Field(...)
    phone: str = Field(...)
    address: str = Field(...)

class UserRegister(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
   
class UserModel(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
    
    
class UpdateUserModel(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
    
    
class UserUpdateRequest(BaseModel):
    full_name: str = None
    address: str = None
    username: str = None
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}