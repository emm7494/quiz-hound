from flask import Blueprint, flash, redirect, render_template, url_for
from ..forms import auth
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    title = 'Sign In'
    form = auth.LoginForm()
    if form.validate_on_submit():
        flash(
            f'Login successful with username: {form.username.data} and remember_me: {form.remember_me.data}')
        return redirect(url_for('index.index'))
    return render_template('auth/login.html', title=title, form=form)
