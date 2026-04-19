from datetime import datetime

from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired 
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

class NewsForm(FlaskForm):
    title = StringField('Название новости', validators=[DataRequired(message='Поле не должно быть пустым'), Length(max=255, message='Заголовок не должен превышать 256 символов')])

    text = TextAreaField('Описание новости', validators=[DataRequired(message='Поле не должно быть пустым')])
    submit = SubmitField('Добавить')

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

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    news = db.relationship('News',back_populates='category')

db.create_all()

@app.route('/')
def home_page():
    news_list = News.query.all()
    return render_template('index.html', news=news_list)

@app.route('/news_detail/<int:id>')
def news_detail(id):
    news_d = News.query.get(id) 
    return render_template('news_detail.html', news_d=news_d)

@app.route('/add_news', methods= ['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('news_detail', id = news.id))
    return render_template('add_news.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)