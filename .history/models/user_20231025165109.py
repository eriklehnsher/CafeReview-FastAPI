
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr



class UserInDB(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

class UserRegister(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
   