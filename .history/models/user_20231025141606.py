from pydantic import BaseModel, Field, EmailStr
from pyObjectId import *

class UserInDB(BaseModel):
    id: PyObjectId = Field(alias="_id")
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}