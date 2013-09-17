from flask import Blueprint, render_template, current_app


rules = Blueprint('rules', __name__)
rules.menu = 'rules'

@rules.route('/rules')
def rules_page():
    return render_template('rules.html', menu=current_app.menu)
