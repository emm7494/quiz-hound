from flask import render_template
from flask_login import login_required

from app.main import bp


@bp.route('/', methods=('GET',))
@bp.route('/index', methods=('GET',))
@login_required
def index():
    posts = {}
    return render_template('main/index.html', title='Welcome to Quiz Hound!', posts=posts)
