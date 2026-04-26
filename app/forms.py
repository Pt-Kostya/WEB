from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Length, DataRequired 

from .models import Category

def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]

class NewsForm(FlaskForm):
    title = StringField('Название новости', validators=[DataRequired(message='Поле не должно быть пустым'), Length(max=255, message='Заголовок не должен превышать 256 символов')])

    text = TextAreaField('Описание новости', validators=[DataRequired(message='Поле не должно быть пустым')])
    category = SelectField('Категории', choices=get_categories())
    submit = SubmitField('Добавить')