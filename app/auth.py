import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.model import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']
        re_password = request.form['re_pass']
        db = get_db()
        error = None
        if not name:
            error = 'Name is required'
        if not password:
            error = 'Password is required'
        if password != re_password:
            error = 'Check Passwords'
        elif db.execute(
            'SELECT id FROM student WHERE username = ?', (name,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(name)

        if error is None:
            db.execute(
                'INSERT INTO student (id, username, password, user_type, user_dept, user_yr, phone_no) VALUES (?, ?, ?,?, ?,?,?)',
                (2173128, name, generate_password_hash(password), 'S','CSE', '2', '9096333107')
            )
            db.commit()
        flash(error)
        return redirect('auth.signin')

    return render_template('auth/signup.html')
    
 # Search in student and teacher -->> teacher / student access

@bp.route('/signin', methods=('GET', 'POST'))
def signin():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['pass']
        db = get_db()
        error = None
        student = db.execute(
            'SELECT * FROM student WHERE id = ?', (id,)
        ).fetchone()

        if student is None:
            error = 'Incorrect username.'
        elif not check_password_hash(student['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = student['id']
            #return redirect(url_for('blog.index'))

        flash(error)

        return redirect(url_for('teacher.dashboard'))

    return render_template('auth/signin.html')

