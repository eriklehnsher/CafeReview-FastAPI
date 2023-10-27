from fastapi import FastAPI, HTTPException, APIRouter, status, Body
from models.user import UserRegister, UserInDB, UserLogin, UserUpdateRequest, UpdateUserModel
from bson import ObjectId
from schemas.user_schema import list_serial
from db import Users_db
from passlib.context import CryptContext
from models.token import *
from typing import Optional
import datetime
from jose import jwt
from config import settings


router = APIRouter()



def get_hashed_password(password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)

#? get_all_users 
@router.get("/")
async def get_all_users():
    users = await list_serial(Users_db.find())
    return users

# ? get_user_by_id()
@router.get("/{user_id}", response_model=UserInDB)
async def get_user_by_id(user_id: str):
    user = await Users_db.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


# ? Register User
@router.post("/user/register", response_model=UserInDB)
async def register_user(user: UserRegister = Body(...)):
    email = user.model_dump()["email"]
    find_user_in_db = await Users_db.find_one({"email": email})
    if find_user_in_db is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email_already_used"
        )
    else:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = user.model_dump()
        user["password"] = get_hashed_password(user["password"])
        user["role"] = "customer"
        user["createdAt"] = now
        new_user = await Users_db.insert_one(user)
        created_user = await Users_db.find_one({"_id": new_user.inserted_id})
        return created_user


# ? Login User
def verify_password(password: str, hashed_password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(
        password, hashed_password
    )


async def authenticate_user(email: str, password: str):
    user = await Users_db.find_one({"email": email})
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


@router.post("/user/login", response_model=Token)
async def login(user_data: UserLogin = Body(...)):
    user_data = user_data.model_dump()
    user = await authenticate_user(user_data["email"], user_data["password"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(minutes=300)
    if user["role"] == "admin":
        access_token_expires = datetime.timedelta(minutes=600)
    access_token = create_access_token(
        data={"sub": user["email"], "role": user["role"], "name": user["username"]},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


#? Update_userInfors by id

@router.put("/{user_id}", response_model=UserInDB)
async def update_user(user_id: str, updated_user:UserUpdateRequest = Body(...)):
    existing_user = await Users_db.find_one({"_id": ObjectId(user_id)})
    if existing_user is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )
        # Cập nhật các trường trong existing_user dựa trên updated_user
    updated_data = updated_user.model_dump(exclude_unset=True)
    for field in updated_data:
        if field in existing_user:
            existing_user[field] = updated_data[field]

    # Lưu người dùng đã cập nhật
    await Users_db.update_one({"_id": ObjectId(user_id)}, {"$set": existing_user})
    return existing_user