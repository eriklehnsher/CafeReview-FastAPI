from fastapi import FastAPI, HTTPException, APIRouter
from models.user import UserRegister, UserInDB, HashedPassword

router = APIRouter()

@router.post("/users/", response_model=UserInDB)
async def create_user(user: UserRegister):

    user_in_db = UserInDB(**user.model_dump(), hashed_password="hashed_password_here")
    return user_in_db
