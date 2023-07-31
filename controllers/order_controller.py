from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Item, Order, OrderItem
from app import db

orders_blueprint = Blueprint("orders", __name__)

# all the orders with create new order button
@orders_blueprint.route("/orders/new")
def new_orders():
    users = User.query.all()
    items = Item.query.all()
    return render_template("orders/new.jinja", users=users, items=items)


@orders_blueprint.route("/orders", methods=["POST"])
def add_orders():
    user_id = request.form['user_id']
    notes = request.form['notes']

    user = User.query.get(user_id)
    order = Order(user=user, notes=notes)
    db.session.add(order)
    db.session.commit()
    # loop through the items, if the item.id is in request.form, create an order_item
    items = Item.query.all()
    for item in items:
        if str(item.id) in request.form:
            kitchen_order = OrderItem(order=order, item=item)
            db.session.add(kitchen_order)
            db.session.commit()     
    return redirect('/orders/new')

# @orders_blueprint.route("/users/<id>/my_order", methods=["POST"])
# def my_order(id):
#     users = User.query.get(id)
#     orders = Order.query.join(User).filter(User.id == id)
#     items = Item.query.join(OrderItem).filter(OrderItem.order_id == id)
#     return render_template("/orders/index.jinja", users = users, orders=orders, items = items)
