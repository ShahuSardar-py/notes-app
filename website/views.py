from flask import Blueprint, render_template

views =Blueprint('views', __name__) #name views taken from file name views

@views.route('/')
def home():
    return render_template("home.html")
