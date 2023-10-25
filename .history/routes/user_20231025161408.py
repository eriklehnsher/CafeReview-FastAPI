from fastapi import FastAPI, HTTPException, APIRouter, status, Body
from models.user import UserRegister, UserInDB, HashedPassword
from bson import ObjectId
from db import db, users_collection
import datetime
from passlib.context import CryptContext


router = APIRouter()
new_id = ObjectId()


def get_hashed_password(password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)

router.post("/user/register", response_model=UserInDB)
async def create_user(user: UserRegister = Body(...)):
    email = user.model_dump()["email"]
    find_user_in_db = await db["Users"].find_one({"email": email})
    if find_user_in_db is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email_already_used")
    else:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = user.model_dump()
        user["password"] = get_hashed_password(user["password"])

        user["createdAt"] = now
        new_user = await db['Users'].insert_one(user)
        created_user = await db["Users"].find_one({"_id": new_user.inserted_id})

        # send email
      
        return created_user
