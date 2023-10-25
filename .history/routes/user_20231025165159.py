from fastapi import FastAPI, HTTPException, APIRouter, status, Body
from models.user import UserRegister, UserInDB
from bson import ObjectId
from schemas.user_schema import list_serial
from db import colection_name




router = APIRouter()

@router.get('/')
async def get_user():
    users = list_serial(colection_name.find())
    return users

@router.post('/register',response_model=UserInDB )
async def register_user(user: UserRegister):
    colection_name.insert_one(dict(user))