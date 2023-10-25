
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr



class User(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    
   