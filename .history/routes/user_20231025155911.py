from fastapi import FastAPI, HTTPException, APIRouter
from models.user import UserRegister, UserInDB, HashedPassword
from bson import ObjectId
from db import db, users_collection

router = APIRouter()
new_id = ObjectId()

@router.post("/users/", response_model=UserInDB)
