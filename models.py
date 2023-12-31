from app import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Integer)
    category = db.Column(db.String(64))
    orders = db.relationship('OrderItem', backref='item')

    def __repr__(self):
        return f"<Item: {self.id}: {self.name}>"
    
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone = db.Column(db.VARCHAR(20))
    address = db.Column(db.String(64))
    orders = db.relationship('Order', backref='user')

    def __repr__(self):
        return f"<User: {self.id}: {self.name}>"

class Order(db.Model):
    # one user orders multiple items
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    items = db.relationship('OrderItem',backref='order', cascade="all, delete")
    notes = db.Column(db.Text())
    def has_item(self, item_id):
        for order_item in self.items:
            if order_item.item_id == item_id:
                return True
        return False
        # return item_id in [order_item.item_id for order_item in self.items]
    def get_item_quantity(self, item_id):
        for order_item in self.items:
            if order_item.item_id == item_id:
                return order_item.quantity
        return 0
        

    def __repr__(self):
        return f"<Order: {self.id}: {self.notes}>"

class OrderItem(db.Model):
    # this joins an Order with multiple Items
    __tablename__ = "order_items"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    quantity = db.Column(db.Integer, nullable=False, default=1)
    def __repr__(self):
        return f"<OrderItem: {self.order_id}>"