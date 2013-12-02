import importlib
from flask import Flask, render_template, request, session, url_for, redirect
from common.db import Db
import hashlib

modules = 'home', 'rules', 'movielist', 'history', 'score'

app = Flask('movienights')
app.db = Db('db/movienights.db')
app.menu = []
for module in list(modules):
    m = importlib.import_module('.'.join(['modules', module]))
    blueprint = m.__dict__[module]
    if blueprint.menu is not None:
        app.menu.append(blueprint.menu)
    app.register_blueprint(blueprint)

def validate_login(username, password):
    res = app.db.query('SELECT id FROM users '
                       'WHERE username = "{0}" AND password = "{1}"'.format(
                       username,hashlib.sha256(password).hexdigest()))
    if len(res) == 1:
        return True
    return False

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/home')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if validate_login(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'This_is_a_very_secure_key!'

if __name__ == '__main__':
    app.run(port=1337, debug=False)
