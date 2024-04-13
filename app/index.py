import hashlib
from flask import render_template, request, redirect
import dao
from app import app, login
from app.model import User
from flask_login import login_user, logout_user
from app import db


@app.route("/")
def index():
    cats = dao.get_categories()
    pros = dao.get_news()
    return render_template('index.html', categories=cats, news=pros)


@app.route("/login")
def loginn():
    return render_template('login.html')


@app.route("/admin/login", methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username, password)
    if user:
        login_user(user)

    return redirect("/admin")


@app.route("/login/signup", methods=['post'])
def signup():
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    check = User.query.filter(User.name.contains(username))
    if username == check:
        pass
    else:
        c = User(name=name, username=username, password=password)
        db.session.add(c)
        db.session.commit()
    return redirect("/login")


@app.route("/login/signin", methods=['post'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username, password)
    if user:
        login_user(user)
        return redirect("/")
    else:
        return redirect("/login")


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route("/logout")
def logout():
    if load_user:
        logout_user()
    return redirect('/')


if __name__ == '__main__':
    from app import admin

    app.run(host='0.0.0.0', debug=True)
