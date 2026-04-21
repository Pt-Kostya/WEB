from datetime import datetime

from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Length, DataRequired 
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mkhdfgldfglsdflvgsdfsdfgh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable= False)
    text = db.Column(db.Text, nullable= False)
    created_date = db.Column(db.DateTime, default=datetime.now)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', back_populates='news')

    def __repr__(self):
        return f'News {self.id}: ({self.title})'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    news = db.relationship('News',back_populates='category')

    def __repr__(self):
        return f'Category {self.id}: ({self.title})'

db.create_all()

def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]

class NewsForm(FlaskForm):
    title = StringField('Название новости', validators=[DataRequired(message='Поле не должно быть пустым'), Length(max=255, message='Заголовок не должен превышать 256 символов')])

    text = TextAreaField('Описание новости', validators=[DataRequired(message='Поле не должно быть пустым')])
    category = SelectField('Категории', choices=get_categories())
    submit = SubmitField('Добавить')

@app.route('/')
def home_page():
    news_list = News.query.all()
    categories= Category.query.all()
    return render_template('index.html', news=news_list, categories=categories)

@app.route('/news_detail/<int:id>')
def news_detail(id):
    news_d = News.query.get(id)
    categories = Category.query.all()
    return render_template('news_detail.html', news=news_d, categories=categories)

@app.route('/add_news', methods= ['GET', 'POST'])
def add_news():
    form = NewsForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        news.category_id = form.category.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('news_detail', id = news.id))
    return render_template('add_news.html', form=form, categories=categories)

@app.route('/category/<int:id>')
def news_in_category(id):
    category = Category.query.get(id)
    news = category.news
    category_name = category.title
    categories = Category.query.all()
    return render_template('category.html', news=news, category_name=category_name, categories=categories)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)