from flask import Blueprint, render_template, current_app
from common import db

movielist = Blueprint('movielist', __name__)
movielist.menu = 'Movie List'
moviedb = db.Db()

@movielist.route('/Movie List')
def movielist_page():
    movies = moviedb.query('SELECT * FROM movies')
    return render_template('movielist.html', menu=current_app.menu,
                            movies=movies)
