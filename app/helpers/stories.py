from app.db import mongo

def create_story(story_data):
    mongo.stories.insert_one(story_data)