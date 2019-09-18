from flask import render_template

from app.main import bp


@bp.route('/', methods=('GET',))
def index():
    title = 'Welcome to Quiz Hound!'
    return render_template('main/index.html', title=title)
