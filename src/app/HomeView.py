from flask import Blueprint, render_template


Home = Blueprint('home', __name__)


@Home.route('/')
def test():
    return render_template("test.html")
