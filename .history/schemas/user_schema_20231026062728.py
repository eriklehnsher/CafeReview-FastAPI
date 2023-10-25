def individual_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["password"],

    }

async def list_serial(users) -> list:
 return  [ await individual_serial(user) for user in users]
