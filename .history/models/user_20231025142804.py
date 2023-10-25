from pydantic import BaseModel, Field, EmailStr
from pyObjectId import *


class UserInDB(BaseModel):
    id: ObjectId = Field(alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

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
        schema_extra = {
            "example": {
                "username": "user_01",
                "email": "user_01@gmail.com",
                "password": "user_01",
            }
        }


class UserModel(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "ADMIN",
                "email": "admin@gmail.com",
                "password": "admin",
            }
        }


class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "admin@gmail.com",
                "password": "admin",
            }
        }
