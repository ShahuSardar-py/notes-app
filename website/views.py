from flask import Blueprint, render_template, request,flash, jsonify
from flask_login import  login_required,  current_user
from .models import Note
from website import db
import json
views =Blueprint('views', __name__) #name views taken from file name views

@views.route('/' , methods=["GET", "POST"])
@login_required
def home():
    if request.method =="POST":
        note = request.form.get("notes")
        if note:

            new_note =Note(data= note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("added new note", category="success")

 
    return render_template("home.html", user= current_user)

@views.route('/delete-note', methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteID = note['noteID']
    print(f"Trying to delete note with ID: {noteID}")  # Debugging statement
    note = Note.query.get(noteID)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            print(f"Deleted note with ID: {noteID}")  # Debugging statement
        else:
            print("User does not have permission to delete this note.")
    else:
        print("Note not found.")
    
    return jsonify({})

