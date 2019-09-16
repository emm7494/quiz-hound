from flask import Blueprint, redirect, render_template

bp = Blueprint('index', __name__)


@bp.route('/', methods=('GET',))
def login():
    return render_template('index.html')
