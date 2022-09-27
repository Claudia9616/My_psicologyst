from flask import render_template, session, flash, redirect, url_for

from app.forms import LoginForm
from app.helpers.users import get_user
from app.models import UserData

from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    context = {
        'login_form': LoginForm()
    }

    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user_doc = get_user(email)

        if user_doc:
            password_db = user_doc['password']

            if password == password_db:
                user_data = UserData(email, password)

        flash('User registered successfully')

        return redirect(url_for('index'))

    return render_template('login.html', **context)
