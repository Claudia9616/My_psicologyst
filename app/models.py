from flask_login import UserMixin

from app.helpers.users import get_user_by_key

class UserData:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

class UserSignUp(UserData):
    def __init__(self, email, password, first_name, last_name, id_number, age, gender) -> None:
        super().__init__(email, password)
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.age = age
        self.gender = gender

class UserModel(UserMixin):
    def __init__(self, user_data: UserData) -> None:
        self.id = user_data.email
        self.password = user_data.password

    @staticmethod
    def query(email):
        user_doc = get_user_by_key(email)
        user_data = UserData(
            email=user_doc["email"],
            password=user_doc["password"]
        )

        return UserModel(user_data)

