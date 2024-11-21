from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_user, current_user

from app.extensions import db, bcrypt
from app.models.user import User
from app.forms import RegistrationForm, LoginForm

from app.models.post import Post
# from app.models.post import Post
# from app.functions import save_picture


user = Blueprint('user', __name__)


@user.route('/user/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, login=form.login.data, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"Поздравляем, {form.login.data}! Регистрация прошла успешно", category="success")
            return redirect(url_for('user.login'))
        except Exception as e:
            print(str(e))
            flash(f"При регистрации произошла ошибка", category="danger")
    else:
        return render_template('user/register.html', form=form)


@user.route('/user/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f"Поздравляем, {form.login.data}! Авторизация прошла успешно", category="success")
            return redirect(next_page) if next_page else redirect(url_for('post.all_auth'))
        else:
            flash(f"Неверный логин или пароль", category="danger")
    return render_template('user/login.html', form=form)


@user.route('/user/lk', methods=['POST', 'GET'])
def lk():
    return render_template('user/lk.html')
