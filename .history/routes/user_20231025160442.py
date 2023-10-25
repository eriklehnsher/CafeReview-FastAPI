from fastapi import FastAPI, HTTPException, APIRouter
from models.user import UserRegister, UserInDB, HashedPassword
from bson import ObjectId
from db import db, users_collection

router = APIRouter()
new_id = ObjectId()

@router.post("/register/", response_model=UserInDB)
async def register_user(user: UserRegister):
    new_id  = ObjectId()
    user_data = user.model_dump()

# Lưu thông tin người dùng vào MongoDB với id tạo mới
    user_in_db = UserInDB(id=new_id, **user_data)
    users_collection.insert_one(user_in_db.model_dump())
    return user_in_db
