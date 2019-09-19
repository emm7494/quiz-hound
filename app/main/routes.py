from flask import render_template
from flask_login import current_user, login_required
from app.models import User
from datetime import datetime
from app.models import db
from app.main import bp


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


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
