from fastapi import FastAPI, HTTPException, APIRouter, status, Body
from models.user import UserRegister, UserInDB
from bson import ObjectId
from schemas.user_schema import list_serial
from db import colection_name
from passlib.context import CryptContext
from models.token import *
from typing import Optional
import datetime





router = APIRouter()


# ? Register User
def get_hashed_password(password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)


@router.get("/")
async def get_user():
    users = list_serial(colection_name.find())
    return users


@router.post("/register", response_model=UserInDB)
async def register_user(user: UserRegister = Body(...)):
    email = user.model_dump()["email"]
    find_user_in_db = colection_name.find_one({"email": email})
    if find_user_in_db is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email_already_used"
        )
    else:
        user = user.model_dump()
        user["password"] = get_hashed_password(user["password"])
        new_user = colection_name.insert_one(user)
        created_user = colection_name.find_one({"_id": new_user.inserted_id})
        return created_user


# ? Login User
def verify_password(password: str, hashed_password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(
        password, hashed_password
    )


async def authenticate_user(email: str, password: str):
    user = colection_name.find_one({"email": email})
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm="HS256")
    return encoded_jwt