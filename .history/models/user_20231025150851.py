from pydantic import BaseModel

class UserInDB(BaseModel):
    id: str  # Assuming you are using strings for user IDs
    username: str
    email: str
    hashed_password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class HashedPassword(BaseModel):
    password: str
