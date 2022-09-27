from flask_login import UserMixin

from app.helpers.users import get_user

class UserData:
    def __init__(self, user_email, password) -> None:
        self.user_email = user_email
        self.password = password

class UserModel(UserMixin):
    def __init__(self, user_data: UserData) -> None:
        self.id = user_data.user_email
        self.password = user_data.password

    @staticmethod
    def query(user_email):
        user_doc = get_user(user_email)
        user_data = UserData(
            user_email=user_doc.email,
            password=user_doc.password
        )

        return UserModel(user_data)