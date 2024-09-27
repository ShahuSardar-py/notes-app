from website import db, create_app
app = create_app()
with app.app_context():
    db.drop_all()  # Drops all tables
    db.create_all()  # Recreates tables