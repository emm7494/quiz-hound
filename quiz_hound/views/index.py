from flask import Blueprint, redirect, render_template
from ..forms import auth

bp = Blueprint('index', __name__)


@bp.route('/', methods=('GET',))
def index():
    form = auth.LoginForm()
    title = 'Welcome to Quiz Hound!'
    return render_template('index/index.html', title=title, form=form)
