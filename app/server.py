from flask import Flask, render_template, request, jsonify

my_flask_app = Flask(__name__)


@my_flask_app.route('/')
def index():
    return render_template('index.html')


@my_flask_app.route('/registration/')
def registration():
    return render_template('registration.html')

@my_flask_app.route('/add_user/', methods=['POST'])
def add_user():
    print(request.form)
    password = request.form.get('password')
    confirm_password = request.form.get('confrim_password')
    if password != confirm_password:
        return  render_template('index.html')
    return jsonify({'result' : 'ok'})


if __name__ == '__main__':
    my_flask_app.run(debug=True)
