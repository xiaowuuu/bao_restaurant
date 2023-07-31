from flask import Flask, render_template, request, redirect, jsonify
from flask import Blueprint
from models import User, Item, Order, OrderItem
from app import db

kitchen_blueprint = Blueprint("kitchen", __name__)

# display user order by id
@kitchen_blueprint.route("/users/<id>/my_order")
def user_order(id):
    user = User.query.get(id)
    item = Order.query.join(Order).filter(Order.user_id == id)
    order = OrderItem.query.join(OrderItem).filter(OrderItem.order_id == id, OrderItem.item_id == id)
    return render_template("/users/show.jinja", user=user, order=order, item=item)