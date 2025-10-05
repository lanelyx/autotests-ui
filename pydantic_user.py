from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": "1",
    "username": "Zara",
    "email": "email@gmail.com"
}
user = User(**user_data)
print(user)
print(user.is_active)

invalid_user_data = {
    "id": "one",
    "username": "Zara",
    "email": "email@gmail.com"

}

invalid_user = User(**invalid_user_data)
print(invalid_user)


