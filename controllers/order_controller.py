from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Item, Order, Kitchen
from app import db

orders_blueprint = Blueprint("orders", __name__)

# all the orders with create new order button
@orders_blueprint.route("/orders")
def orders():
    orders = Order.query.all()
    users = User.query.all()
    return render_template("orders/new.jinja", orders = orders, users = users)

@orders_blueprint.route("/orders/new", methods=["POST"])
def new_order():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    notes = request.form['notes']
    order = Order(user_id = user_id, item_id = item_id, notes = notes)
    db.session.add(order)
    db.session.commit()
    return redirect('/orders')
