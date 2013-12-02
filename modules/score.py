from flask import Blueprint, render_template, current_app
from common import db

score = Blueprint('score', __name__)
score.menu = 'Score'
moviedb = db.Db()

@score.route('/Score')
def score_page():
    score = moviedb.query('SELECT username, score FROM users ORDER BY username')
    return render_template('score.html', menu=current_app.menu, score=score)
