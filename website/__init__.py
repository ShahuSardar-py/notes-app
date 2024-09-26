from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ideaTribe'  # SECRET_KEY should be a string
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"  # Defining where our SQLAlchemy DB is located
    db.init_app(app)  # Initialize the database

    from .views import views
    from .auth import auth

    # Registering our routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    # Create the database with the app context
    with app.app_context():
        create_database()

    return app

def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all()  # No need to pass 'app' here
        print("Created database")
