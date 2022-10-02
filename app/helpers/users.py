from app.db import mongo

def get_user_by_key(value, key='email'):
    user = mongo.users.find_one({key: value})
    return user

def create_user(user_data):
    mongo.users.insert_one(user_data.__dict__)

def get_user_data(email, data="first_name"):
    user = get_user_by_key(email)
    return user[data]
