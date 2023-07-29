from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/bao_database"
# app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# from seed import seed
# app.cli.add_command(seed)
from models import * 


@app.route("/")
def home():
    return render_template("index.jinja")