import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.speech import recognise_model

bp = Blueprint('teacher', __name__)

@bp.route('/teacher/dashboard', methods=('GET', 'POST'))
def dashboard():
    return render_template('ltr/dashboard.html')

@bp.route('/teacher/test', methods=('GET', 'POST'))
def test():
    return render_template('ltr/index.html')

@bp.route('/teacher/test1', methods=('GET', 'POST'))
def test1():
    return render_template('ltr/test1.html')

@bp.route('/teacher/index', methods=('GET', 'POST'))
def index():
    return render_template('ltr/index.html')

@bp.route('/teacher/VR', methods=('GET', 'POST'))
def vr():
    obj_no = recognise_model()
    #obj_no = 0
    return render_template('ltr/vr.html', obj_no = obj_no)

@bp.route('/', methods=('GET', 'POST'))
def head():
    return render_template('ltr/head.html')