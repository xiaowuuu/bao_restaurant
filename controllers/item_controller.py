from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Item, Order, Kitchen
from app import db

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def items():
    items = Item.query.all()
    return render_template("items/index.jinja", items=items)