from fastapi import FastAPI, HTTPException
from models.user import UserRegister, UserInDB, HashedPassword

router = FastAPI()

@router.post("/users/", response_model=UserInDB)
async def create_user(user: UserRegister):
    # Thực hiện quá trình tạo tài khoản và lưu vào cơ sở dữ liệu
    # Trả về thông tin người dùng đã tạo
    # Xử lý lưu trữ mật khẩu đã băm vào cơ sở dữ liệu
    user_in_db = UserInDB(**user.model_dump(), hashed_password="hashed_password_here")
    return user_in_db
