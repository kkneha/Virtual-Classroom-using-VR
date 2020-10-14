import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('teacher', __name__, url_prefix='/teacher')

@bp.route('/dashboard', methods=('GET', 'POST'))
def dashboard():
    return render_template('ltr/dashboard.html')

@bp.route('/test', methods=('GET', 'POST'))
def test():
    return render_template('ltr/test.html')

@bp.route('/test1', methods=('GET', 'POST'))
def test1():
    return render_template('ltr/test1.html')