from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/bao_database"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
from models import * 
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)


from controllers.user_controller import users_blueprint
from controllers.item_controller import items_blueprint


app.register_blueprint(users_blueprint)
app.register_blueprint(items_blueprint)

@app.route("/")
def home():
    return render_template("index.jinja")

if __name__ == '__main__':
    app.run(debug=True)