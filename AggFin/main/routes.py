import requests
from flask import Blueprint, render_template, request


main = Blueprint('main', __name__)


# Home route displaying stock info 
@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():

    bg_color = 'white'  

    if request.method == 'POST':
        stock_name = request.form.get('stock_name')
        bg_color = request.form.get('bg_color', 'white')  
        
