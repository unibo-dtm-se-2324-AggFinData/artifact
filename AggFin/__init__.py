from flask import Flask
from AggFin.routes import main


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MohJJAMhsi58ubsc9a6xas4adwdnsaxaxSS'
    
    app.register_blueprint(main)



    return app