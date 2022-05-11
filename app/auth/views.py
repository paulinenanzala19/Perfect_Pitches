from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,logout_user,login_required
from .. import db
from ..email import mail_message


@auth.route('/login',methods=['GET','POST'])
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

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Karibu perfect pitches","email/welcome",user.email,user=user)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/registration.html',registration_form = form)

    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))