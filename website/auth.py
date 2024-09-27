from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth =Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =="POST":
        email= request.form.get("email")
        password= request.form.get("password")

        #query db
        user= User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in sucessfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password!" , category="error")
        else:
            flash("No user found", category="error")

             





    return render_template("login.html", user= current_user)

@auth.route('/logout')
@login_required #decorator to ensure that only logged in will see logout option
def logout():
    logout_user()
    flash("logged out", category="success")


    return redirect(url_for("auth.login"))

@auth.route('/signup' ,methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') #email is variable. .get('xx') is the name of that input feild in the HTML
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user= User.query.filter_by(email=email).first()
        if user:
            flash("already exists!", category="error")
        elif len(email)<4:
            flash('EMail needs to be longer' , category='error')
        elif len(firstName) < 2:
            flash('Enter a longer name', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 5:
            flash('password needs to be more than 5 characters', category='error')
        else:
            new_user= User(email= email, first_name=firstName, password=generate_password_hash(password1, method= 'pbkdf2:sha256')) #User is the one desinfed in models
            db.session.add(new_user)
            db.session.commit()
            flash('account created!' ,category='success')
            login_user(new_user, remember=True)
            return redirect(url_for("views.home")) #redirects to the home function that will be found in the views.py
        



    return render_template("signup.html",  user= current_user)