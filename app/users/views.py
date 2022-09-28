from werkzeug.security import generate_password_hash 

from flask import render_template, session, flash, redirect, url_for

from app.db import mongo
from app.forms import CreateUser

from . import users

users_collection = mongo.users

@users.route('/signup', methods=['GET', 'POST'])
def signup():
    create_user = CreateUser()

    context = {
        'create_user': CreateUser()
    }

    if create_user.validate_on_submit():
        email = create_user.email.data
        
        user_doc = users_collection.find_one({"email": email})

        if not user_doc:
            username = create_user.username.data
            password = create_user.password.data

            users_collection.insert_one({
                "email": email,
                "username": username,
                "password": password
            })

        else:
            flash("The user already exist!")
    
    return render_template('signup.html', **context)