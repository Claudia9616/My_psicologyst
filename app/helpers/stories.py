from app.db import mongo

def create_story(story_data):
    mongo.stories.insert_one(story_data)

def get_best_stories():
    stories = mongo.stories.find({
        "recommendation": "Yes",
        "score": "Good"
    })

    return stories