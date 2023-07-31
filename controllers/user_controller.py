from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Item, Order, OrderItem
from app import db

users_blueprint = Blueprint("users", __name__)

# display user list, next is link to user's order
@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users=users)

# # display user order by id
# @users_blueprint.route("/users/<id>/my_order")
# def user_order(id):
#     user = User.query.get(id)
#     item = Item.query.get(id)
#     return render_template("/users/show.jinja", user=user, item=item)