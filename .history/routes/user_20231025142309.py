from fastapi import APIRouter, Body, Depends, status, HTTPException
from models.user import UserLogin, UserModel, UserInDB, UserRegister
from fastapi.encoders import jsonable_encoder
from db import db
from bson import ObjectId