
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from models.pyObjectId import *


class User(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    
   