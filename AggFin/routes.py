from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
<<<<<<< HEAD
    return render_template('home.html')
=======
    return render_template('home.html')
    

@main.route("/about")
def about():
    return render_template('about.html')
>>>>>>> login-register-pages
