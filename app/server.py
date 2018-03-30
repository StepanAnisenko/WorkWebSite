from flask import Flask, render_template, request

my_flask_app = Flask(__name__)


@my_flask_app.route('/')
def index():
    return render_template('index.html')


@my_flask_app.route('/registration/')
def all_news():
    return render_template('registration.html')


if __name__ == '__main__':
    my_flask_app.run(debug=True)
