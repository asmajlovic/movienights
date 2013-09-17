from flask import Blueprint, render_template, current_app


home = Blueprint('home', __name__)
home.menu = None

@home.route('/home')
def homepage():
    return render_template('home.html', menu=current_app.menu)
