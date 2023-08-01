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
    phone = db.Column(db.Integer)
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

    def __repr__(self):
        return f"<Order: {self.id}: {self.notes}>"

class OrderItem(db.Model):
    # this joins an Order with multiple Items
    __tablename__ = "order_items"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    def __repr__(self):
        return f"<OrderItem: {self.order_id}>"