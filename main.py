import os

from flask import render_template
from flask_login import login_required, current_user

from app import create_app
from app.helpers.users import get_user_data
from app.helpers.stories import get_best_stories

app = create_app()

@app.route('/', methods=['GET'])
def index():

    stories = get_best_stories()

    print(stories)

    context = {
        "stories": stories
    }

    return render_template('index.html', **context)

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    email = current_user.id

    context = {
        'username': get_user_data(email)
    }

    return render_template('home.html', **context)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)