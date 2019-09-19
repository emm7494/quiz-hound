from flask import render_template, request
from flask_login import current_user, login_required
from app.models import User
from datetime import datetime
from app.models import db
from app.main import bp
from app.main.forms import EditProfileForm


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/edit_profile')
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        return render_template(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('main/edit_profile.html', title='Edit Profile', form=form)


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
    return render_template('main/user.html', title='Profile', user=user, posts=posts)
