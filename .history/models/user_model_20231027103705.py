from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str

    user = User(username="example_user", email="user@example.com")


# Chuyển đổi đối tượng user thành từ điển
user_dict = user.dict()
print(user_dict)
