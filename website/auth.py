from flask import Blueprint, render_template, request, flash

auth =Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signup' ,methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') #email is variable. .get('xx') is the name of that input feild in the HTML
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)<4:
            flash('EMail needs to be longer' , category='error')
        elif len(firstName) < 2:
            flash('Enter a longer name', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 5:
            flash('password needs to be more than 5 characters', category='error')
        else:
            
            flash('account created!' ,category='success')



    return render_template("signup.html")