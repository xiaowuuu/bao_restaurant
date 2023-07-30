from flask import Flask, render_template, request, redirect, jsonify
from flask import Blueprint
from models import User, Item, Order, Kitchen
from app import db

items_blueprint = Blueprint("items", __name__)

@items_blueprint.route("/items")
def items():
    items = Item.query.all()
    return render_template("items/index.jinja", items=items)

#     # get category
# @items_blueprint.route('/items', methods=['GET'])
# def get_item_by_category():
#     categories = set(item['category'] for item in items)
#     categories_items = {}

#     for category in categories:
#         items_in_category = [item['name'] for item in items if item['category'] == category]
#         categories_items[category] = items_in_category

#     return jsonify(categories_items)