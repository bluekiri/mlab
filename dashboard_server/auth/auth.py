from flask import flash
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.utils import redirect

from dashboard_server.app import app

app.route('/login', methods=['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('_login_user.html', error=error)
