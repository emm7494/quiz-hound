from flask import Blueprint, flash, redirect, render_template, url_for
from app.auth.forms import LoginForm
from app.auth import bp
from flask_login import current_user, login_user, logout_user
from app.models import User


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.check_password(form.password.data):
            flash(f'Invalid username or password!')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
    return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    redirect(url_for('main.index'))
