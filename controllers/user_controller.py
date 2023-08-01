from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Item, Order, OrderItem
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users/new", methods=["POST"])
def new_user():
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    db.session