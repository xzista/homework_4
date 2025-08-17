# Веб-приложение на Django

## Описание проекта
Этот проект представляет собой веб-приложение на Django, которое будет постепенно дополняться в рамках следующих домашних заданий. На текущем этапе реализованы:

- Главная страница (`/home/`)
- Страница контактов (`/contacts/`) с формой обратной связи
- Базовая обработка POST-запросов

## 📂 Структура проекта
```
homework_4/
├── catalog/
│   ├── migrations/
│   │   └── __int__.py
│   ├── static/
│   │   └── catalog/
│   │       └── images/
│   │           ├── image_navbar.png
│   │           └── photo.png
│   ├── templates/
│   │   └── catalog/
│   │       ├── contacts.html
│   │       └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .flake8
├── .gitignore
├── manage.py
├── poetry.lock
├── pyproject.toml
└── README.md
```
## 🚀 Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/xzista/homework_4
cd project2
```
2. Установите зависимости:
```bash
poetry install
```
3. Примените миграции:
```bash
python manage.py migrate
```
4. Запустите сервер:
```bash
python manage.py runserver
```

## 📌 Функциональность

Реализовано:

- Маршрутизация между страницами

- Форма обратной связи

- Обработка POST-запросов

- Базовая статика (Изображения)

## 🛠 Технологический стек

- Python 3.13
- Django 5.2.5 и выше
- Bootstrap 5
- HTML5/CSS3