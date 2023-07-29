from app import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Integer)
    category = db.Column(db.String(64))
    orders = db.relationship('Kitchen', backref='item')

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
    kitchen = db.relationship('Kitchen',backref='order')
    notes = db.Column(db.Text())

    def __repr__(self):
        return f"<Order: {self.id}: {self.notes}>"

class Kitchen(db.Model):
    # this joins an Order with multiple Items
    __tablename__ = "kitchen side"
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)

    def __repr__(self):
        return f"<Kitchen: {self.order_id}>"