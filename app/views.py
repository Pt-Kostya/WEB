from flask import render_template, url_for, redirect

from . import app, db
from .models import News, Category
from .forms import NewsForm

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