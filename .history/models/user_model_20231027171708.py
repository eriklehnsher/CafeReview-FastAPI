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
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserRegister(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

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


class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)






class ListUser(BaseModel):
    id: str = Field(...)
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: str = Field(...)
    createdAt: str = Field(...)