from fastapi import FastAPI, HTTPException, APIRouter, status, Body
from models.user import User
from bson import ObjectId
from schemas.user_schema import list_serial
from db import colection_name




router = APIRouter()

@router.get('/')
async def get_user():
    users = list_serial(colection_name.find())
    return users