from flask import render_template,redirect,url_for,flas,request
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from flask_login import login_user
from .. import db


@auth.route('/login' methods=['GET','POST'])
def login():
    signin_form = LoginForm()
    if signin_form.validate_on_submit():
        user = User.query.filter_by(email = signin_form.email.data).first()
        if user is not None and user.verify_password(signin_form.password.data):
            login_user(user,signin_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Pitches login"
    return render_template('auth/login.html',signin_form = signin_form,title=title)
    
