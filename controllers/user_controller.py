from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users/add")
def add_user():
    return render_template("users/new_user.jinja")

@users_blueprint.route("/users/add", methods=["GET","POST"])
def new_user():
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    user = User(name=name, phone=phone, address=address)
    db.session.add(user)
    db.session.commit()
    return redirect("/users")

@users_blueprint.route("/users/delete/<user_id>", methods=["POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect("/users")
    else:
        return "User not found", 404
