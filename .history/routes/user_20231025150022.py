from fastapi import APIRouter, Body, Depends, status, HTTPException
from models.user import UserLogin, UserInDB, UserRegister
from fastapi.encoders import jsonable_encoder
from db import db
from bson import ObjectId
from passlib.context import CryptContext
import datetime

router = APIRouter()


def get_hashed_password(password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)


@router.post("/users/", response_model=UserInDB)
async def create_user(user: UserRegister):
    # Thực hiện quá trình tạo tài khoản và lưu vào cơ sở dữ liệu
    # Trả về thông tin người dùng đã tạo
    # Xử lý lưu trữ mật khẩu đã băm vào cơ sở dữ liệu
    user_in_db = UserInDB(**user.model_dump(), hashed_password="hashed_password_here")
    return user_in_db