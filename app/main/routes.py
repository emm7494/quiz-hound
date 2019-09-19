from flask import render_template
from flask_login import login_required
from app.models import User

from app.main import bp


@bp.route('/', methods=('GET',))
@bp.route('/index', methods=('GET',))
@login_required
def index():
    posts = {}
    return render_template('main/index.html', title='Welcome to Quiz Hound!', posts=posts)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Testing 1'},
        {'author': user, 'body': 'Testing 2'},
    ]
    return render_template('main/user.html', user=user, posts=posts)
