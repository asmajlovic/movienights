from flask import Blueprint, render_template, current_app
from common import db

proposed_movies = Blueprint('proposed_movies', __name__)
proposed_movies.menu = 'Proposed Movies'
moviedb = db.Db()

@proposed_movies.route('/Proposed Movies')
def proposed_movies_page():
    history = moviedb.query('SELECT * FROM proposed_movies ORDER BY date ASC')
    proposed_movies = {}
    for event in history:
        date, title_ids = event[0], event[1:6]
        titles = []
        for title_id in title_ids:
            if title_id is not None:
                titles.append(moviedb.query('SELECT title FROM movies WHERE id = {0}'.format(title_id))[0][0])
        proposed_movies[date] = titles
    return render_template('proposed_movies.html', menu=current_app.menu,
                            proposed_movies=proposed_movies)
