from flask import Blueprint, redirect, render_template
from ..forms import auth
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = auth.LoginForm()
    title = 'Sign In'
    return render_template('auth/login.html', title=title, form=form)
