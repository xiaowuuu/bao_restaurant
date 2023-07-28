from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/bao_database"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    return "welcome to our Bao house."