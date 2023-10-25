
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from models.pyObjectId import *


class User(BaseModel):
    id: PyObjectId = Field(alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    createdAt: str = Field(...)
    
   