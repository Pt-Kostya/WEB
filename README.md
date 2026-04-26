# Новостной портал

Новостной сайт, на котором любой желающий может оставить смешную и не очень новость!

## Описание
Новостной сайт, созданный с исползованием микрофреймворка Flask в рамках обучения по программе Python Expert.

## Стек технологий
* Python
* Flask
* WTForms
* SQLAlchemy

## Как запустить
1. Скопируй репозиторий.
2. Создай и активируй виртуальное окружение.
```commandline
py -m venv .venv
source .venv/Scripts/activate
```
3. Установи зависимости.
```commandline
pip install -r requiremets.txt
```
4. Создай файл .env и укажи настройки подключения к БД и секретный ключ.
```commandline
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
5. Запустите flask приложение.
```commandline
flask run
```
