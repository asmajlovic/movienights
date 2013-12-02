from flask import Blueprint, render_template, current_app
from common import db

history = Blueprint('history', __name__)
history.menu = 'History'
moviedb = db.Db()

@history.route('/History')
def history_page():
    res_history = moviedb.query('SELECT * FROM history ORDER BY date ASC')
    history = {}
    for event in res_history:
        date, title_ids, winner_id = event[0], event[1:6], event[6]
        titles = []
        for title_id in title_ids:
            if title_id is not None:
                title = moviedb.query('SELECT title FROM movies WHERE id = {0}'.format(title_id))[0][0]
                titles.append(title)
                if title_id == winner_id:
                    winner = title
        history[date] = (titles, winner)
    return render_template('history.html', menu=current_app.menu,
                            history=history)
