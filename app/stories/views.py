from flask import render_template, flash
from flask_login import login_required, current_user

from app.forms import SuccessStory
from app.helpers.stories import create_story
from app.helpers.users import get_user_by_key

from . import stories

@stories.route('success_stories', methods=["GET", "POST"])
@login_required
def success_stories():
    success_story_form = SuccessStory()

    context = {
        'success_story_form': success_story_form
    }

    if success_story_form.validate_on_submit():
        email = current_user.id

        user_data = get_user_by_key(email)

        story_data = {
            "email": email,
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "age": user_data["age"],
            "score": success_story_form.score.data, 
            "story": success_story_form.story.data, 
            "recommendation": success_story_form.recommendation.data 
        }

        create_story(story_data)

        flash("Story sended")

    return render_template("success.html", **context)