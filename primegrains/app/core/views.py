from . import bp

from flask import render_template


@bp.route("/")
def index():
    return render_template('index.html')


@bp.route("/delivery")
def delivery():
    return render_template('delivery.html')

