from collections import UserDict
from socket import create_server
from fastapi import APIRouter, Body, Depends, status, HTTPException
from models.user import UserLogin, UserModel, UpdateUserModel,  UserInDB, UserRegister
from fastapi.encoders import jsonable_encoder
from db import db
from bson import ObjectId
from fastapi.responses import JSONResponse
from typing import List, Optional
from passlib.context import CryptContext
from contracts.token import *
import datetime
from jose import jwt
from config import settings
from middleware.get_current_user import get_current_user





router = APIRouter()

def get_hashed_password(password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)

router.post("/user/register", response_model=UserInDB)
async def create_user(user: UserRegister = Body(...)):
    email = user.dict()["email"]
    find_user_in_db = await db["Users"].find_one({"email": email})
    if find_user_in_db is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email_already_used")
    else:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = user.dict()
        user["password"] = get_hashed_password(user["password"])
        user["role"] = "customer"
        user["createdAt"] = now
        new_user = await db['Users'].insert_one(user)
        created_user = await db["Users"].find_one({"_id": new_user.inserted_id})

        # send email
        msg = EmailMessage()
        msg['From'] = email_address
        body ="Chào mừng đến Hanoi Car,"+"\nThông tin tài khoản:"+"\nEmail: " + user["email"]+"\nTên tài khoản: "+user["username"]+"\nVui lòng đăng nhập để sử dụng dịch vụ của chúng tôi."
        msg['Subject'] = 'Welcome to HanoiCar'
        msg['To'] = user["email"]
        msg.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_address, email_password)
            smtp.sendmail(email_address, user["email"], msg.as_string())

        return created_user