from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/team")
def team():
    return render_template('team.html')

@main.route("/donate")
def donate():
    return render_template('donate.html')

@main.route("/test")
def test():
    return render_template('test.html')