from flask import Flask, render_template, request, jsonify
from app.mod_auth.db import User, db_session, Role


my_flask_app = Flask(__name__)


@my_flask_app.route('/')
def index():
    return render_template('index.html')


@my_flask_app.route('/registration/', methods=['GET', 'POST'])
def registration():
    list_of_roles =[]
    roles = Role.query.all()
    for role in roles:
        if role.name != "admin":
            list_of_roles.append(role.name)
    return render_template('registration.html', list_of_roles=list_of_roles)


@my_flask_app.route('/add_user/', methods=['POST'])
def add_user():
    print(request.form)
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    nickname = request.form.get('nickname')
    roles = Role.query.all()
    role_name = request.form.get('role')
    role_id = 2
    for role in roles:
        if role_name == role.name: role_id =role.id

    if password != confirm_password:
        return  render_template('reg_error.html')
    else:
        client = User(first_name, last_name, nickname, password, email, role_id)
        print(client)
        db_session.add(client)
        db_session.commit()

    return render_template("index.html")


if __name__ == '__main__':
    my_flask_app.run(debug=True)
