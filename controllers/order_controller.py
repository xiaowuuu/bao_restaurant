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


# display user list, next is link to user's order
@orders_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users=users)

# create new order
@orders_blueprint.route("/orders/new", methods=["POST"])
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

# order history (only for displaying, could not edit or delete)
@orders_blueprint.route("/users/<id>/history")
def my_order(id):
    user = User.query.get(id)
    orders = Order.query.filter_by(user_id = id)
    return render_template("/users/history.jinja", user=user, orders=orders, )

# order list page
@orders_blueprint.route("/users/<id>/my_orders")
def order_list(id):
    user = User.query.get(id)
    orders = Order.query.filter_by(user_id = id)
    return render_template("orders/order_list.jinja", user=user, orders=orders)

# one order by order id
@orders_blueprint.route("/orders/<id>")
def show_order(id):
    order = Order.query.get(id)
    user = User.query.all()
    orderitems = OrderItem.query.filter_by(order_id = id)
    return render_template("orders/order_by_id.jinja", user = user, order=order, orderitems=orderitems)


# user edit order by order id, render the page first
@orders_blueprint.route("/orders/<id>/edit")
def edit_order(id):
    items = Item.query.all()
    orders = Order.query.get(id)
    return render_template("orders/edit.jinja", orders=orders, items=items)
# # edit
# @orders_blueprint.route("/orders/<id>/edit", methods=['POST'])
# def update_order(id):
#     user_id = request.form['user_id']
#     item = request.form['item']
#     notes = request.form['notes']
#     orders = Order.query.get(id)
    
#     orders.item = item
#     orders.notes = notes
#     orders.user_id = user_id
# # do i need to clear the table first as i can select multiple items?

#     db.session.add(orders)
#     db.session.commit()

#     items = Item.query.all()
#     for item in items:
#         if str(item.id) in request.form:
#             kitchen_order = OrderItem(order=orders, item=item)
#             db.session.add(kitchen_order)
#             db.session.commit()  
#     return redirect("/orders/<id>")

@orders_blueprint.route("/orders/<id>/edit", methods=["post"])
def update_order(id):
    # user_id = request.form['user_id']
    # Order.query.filter(Order.)
    notes = request.form['notes']
    order = Order.query.get(id)
    order.notes = notes
    
    # loop through the items, if the item.id is in request.form, create an order_item
    items = Item.query.all()
    OrderItem.query.filter(OrderItem.order_id == order.id).delete()
    for item in items:

        # else if item not in order, create new OrderItem
        if str(item.id) in request.form:
            kitchen_order = OrderItem(order=order, item=item)
            db.session.add(kitchen_order)
            
    db.session.commit() 

    return redirect(f'/orders/{id}')
# delete order by order id
@orders_blueprint.route("/orders/<id>/delete", methods=['POST'])
def delete_order(id):
    # Order.query.filter_by(id = id).delete()
    order = Order.query.get(id)
    user_id = order.user_id
    db.session.delete(order)
    db.session.commit()
    return redirect(f"/users/{user_id}/my_orders")





