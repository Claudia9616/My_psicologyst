from werkzeug.security import generate_password_hash 

from flask import render_template, flash, redirect, url_for

from app.models import UserSignUp
from app.forms import CreateUser
from app.helpers.users import get_user_by_key, create_user

from . import users

@users.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = CreateUser()

    context = {
        'signup_form': CreateUser()
    }

    if signup_form.validate_on_submit():
        email = signup_form.email.data
        password = signup_form.password.data
        
        user_doc = get_user_by_key(email)

        if not user_doc:
            email = signup_form.email.data
            password_hash = generate_password_hash(password)
            first_name = signup_form.first_name.data
            last_name = signup_form.last_name.data
            id_number = signup_form.id_number.data
            age = signup_form.age.data
            gender = signup_form.gender.data

            user_data = UserSignUp(
                email, 
                password_hash, 
                first_name, 
                last_name,
                id_number,
                age,
                gender
            )

            create_user(user_data)



        else:
            flash("The user already exist!")
    
    return render_template('signup.html', **context)