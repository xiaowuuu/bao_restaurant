from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Item, Order, Kitchen

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users=users)