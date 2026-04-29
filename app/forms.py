from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, PasswordField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo

from .models import Category

def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]

class NewsForm(FlaskForm):
    title = StringField('Название новости', validators=[DataRequired(message='Поле не должно быть пустым'), Length(max=255, message='Заголовок не должен превышать 256 символов')])

    text = TextAreaField('Описание новости', validators=[DataRequired(message='Поле не должно быть пустым')])
    category = SelectField('Категории', choices=get_categories())
    submit = SubmitField('Добавить')

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Некоректный email')])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторить пароль', validators=[DataRequired(), EqualTo('password', message='Пароли не совпадают')])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')


