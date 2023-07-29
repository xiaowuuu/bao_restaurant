from app import db
from models import Item, User
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    User.query.delete()
    Item.query.delete()
    user_1 = User(name="Ying", phone="1234", address="Leith")
    user_2 = User(name="Patrick", phone="54321", address="Leith Walk")
    user_3 = User(name="Holly", phone="23456", address="37 Castle Terrace")

    item_1 = Item(name="Beef Bao", price=3, category="Bao")
    item_2 = Item(name="Tofu Bao (V)", price=3, category="Bao")
    item_3 = Item(name="Bok Choy & Shiitake Mushroom Bao (V)", price=3, category="Bao")

    item_4 = Item(name="Stir Fry Noodles (Chicken)", price=8, category="Noodles")
    item_5 = Item(name="Stir Fry Noodles (V)", price=8, category="Noodles")
    item_6 = Item(name="Zha Jiang Mian", price=9, category="Noodles")

    item_7 = Item(name="Classic Bubble Tea", price=4, category="Bubble Tea")
    item_8 = Item(name="Brown Sugar Bubble Tea", price=5, category="Bubble Tea")
    
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.add(user_3)

    db.session.add(item_1)
    db.session.add(item_2)
    db.session.add(item_3)
    db.session.add(item_4)
    db.session.add(item_5)
    db.session.add(item_6)
    db.session.add(item_7)
    db.session.add(item_8)

    db.session.commit()