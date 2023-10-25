def individual_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["password"],
        "role": user["role"],
    }

async def list_serial(users) -> list:
    user_list = await users.to_list(length=None)
    return [ individual_serial(user) for user in user_list]