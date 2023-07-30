from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Item, Order, Kitchen
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users=users)

# display user's order by id
@users_blueprint.route("/users/<id>/my_order")
def user_order(id):
    users = User.query.get(id)
    items = Item.query.join(Order).filter(Order.user_id == id)
    return render_template("/orders/index.jinja", users = users, items = items)