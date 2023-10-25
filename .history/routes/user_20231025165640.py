from fastapi import FastAPI, HTTPException, APIRouter, status, Body
from models.user import UserRegister, UserInDB
from bson import ObjectId
from schemas.user_schema import list_serial
from db import colection_name




router = APIRouter()




def get_hashed_password(password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)

@router.get('/')
async def get_user():
    users = list_serial(colection_name.find())
    return users

@router.post('/register',response_model=UserInDB )
async def register_user(user: UserRegister  = Body(...)):
    email = user.model_dump()["email"]
    find_user_in_db = await  colection_name.find_one({"email": email})
    if find_user_in_db is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email_already_used")

    else:

        user = user.model_dump()
        user["password"] = get_hashed_password(user["password"])
    
       
        new_user = await colection_name.insert_one(user)
        created_user = await colection_name.find_one({"_id": new_user.inserted_id})
        return created_user