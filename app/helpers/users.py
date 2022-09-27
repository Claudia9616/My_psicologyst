from app.db import mongo

users_collection = mongo.users

def get_user(email):
    return users_collection.find_one({
        'email':email
    })