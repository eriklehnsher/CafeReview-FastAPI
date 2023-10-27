from fastapi import APIRouter, Body, Depends, status, HTTPException
from config import db
from models.user_model import User, UserInDB
import asyncio
import bcrypt
from pydantic import parser as  pydantic_parser





router = APIRouter()

