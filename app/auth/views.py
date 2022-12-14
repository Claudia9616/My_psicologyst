from werkzeug.security import check_password_hash

from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user

from app.forms import LoginForm
from app.helpers.users import get_user_by_key
from app.models import UserData, UserModel

from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    context = {
        'login_form': LoginForm()
    }
    
    if current_user.is_authenticated:
        flash("Already logged in")
        return redirect(url_for('home'))

    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user_doc = get_user_by_key(email)

        if user_doc:
            password_from_db = user_doc["password"]

            if check_password_hash(password_from_db, password):
                user_data = UserData(email, password)
                user = UserModel(user_data)

                login_user(user)
                redirect(url_for('home'))
            else:
                flash("Incorrect username or password")

        else:
            flash("User does not exist")

        flash('User registered successfully')

        return redirect(url_for('home'))

    return render_template('login.html', **context)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
