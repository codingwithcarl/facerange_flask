from flask import render_template, Blueprint


main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template('index.html')


@main.route("/about")
def about():
    return render_template('about.html', title='About')
