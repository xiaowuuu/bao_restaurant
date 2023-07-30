from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Item, Order, Kitchen
from app import db

orders_blueprint = Blueprint("orders", __name__)

# all the orders with create new order button
@orders_blueprint.route("/orders/new")
def new_orders():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    notes = "notes" in request.form
    order = Order(user_id = user_id, notes = notes)
    kitchen = Kitchen(item_id = item_id)
    db.session.add(kitchen)
    db.session.add(order)
    db.session.commit()
    return redirect('/orders')
    # orders = Order.query.all()
    # users = User.query.all()
    # items = Item.query.all()
    # return render_template("orders/new.jinja", orders = orders, users = users, items = items)

# @orders_blueprint.route("/orders/new", methods=["POST"])
# def new_order():
#     user_id = request.form['user_id']
#     item_id = request.form['item_id']
#     notes = request.form['notes']
#     order = Order(user_id = user_id, item_id = item_id, notes = notes)
#     db.session.add(order)
#     db.session.commit()
#     return redirect('/orders')

