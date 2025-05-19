from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_migrate import Migrate
from AggFin.routes import main
from .auth import auth as users_blueprint


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MohJJAMhsi58ubsc9a6xas4adwdnsaxaxSS'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example for SQLite

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    # make sure 
    from AggFin.users.forms import users
   

    from AggFin.users.routes import users
    from AggFin.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(main)
     
    app.register_blueprint(users_blueprint)
    

    return app
