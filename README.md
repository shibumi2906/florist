# Florist — Django Flower Shop

A Django-based flower shop web application with a product catalog, user registration, order management, and an experimental Telegram bot integration.

The project demonstrates the development of a traditional server-side web application, including database models, authentication, Django templates, sessions, order handling, and an additional Telegram-based interface.

## Features

- flower catalog browsing;
- individual product pages;
- user registration and authentication;
- adding products to a shopping cart;
- session-based cart storage;
- creating and viewing orders;
- product management through Django Admin;
- product image upload and display;
- Telegram bot for catalog interaction and order creation;
- basic Django automated tests.

## Architecture

The application is split into several Django modules:

```text
florist/
├── catalog/          # product catalog and cart logic
├── orders/           # user orders
├── users/            # registration and user management
├── flowershop/       # Django project configuration
├── telegram_bot/     # Telegram interface
├── templates/        # HTML templates
├── static/           # CSS and static assets
├── media/            # product images
└── manage.py
```

### Catalog

Handles product storage and presentation. Each catalog item contains a name, description, price, and image.

The catalog provides product listing, product detail pages, and cart functionality.

### Orders

Contains the order model and order-related logic.

Orders are associated with registered users and products and include:

- product quantity;
- order status;
- creation date;
- user association.

### Users

Uses Django's built-in authentication system together with a custom registration form that includes email.

### Telegram Bot

The project also contains a prototype Telegram interface with:

- `/start` command;
- shop navigation menu;
- catalog retrieval;
- product selection;
- delivery address input;
- order creation.

The Telegram integration is experimental and requires additional configuration before being used outside the original local development environment.

## Tech Stack

- Python
- Django 4.2
- Django ORM
- SQLite
- Django Templates
- HTML / CSS
- Pillow
- Django REST Framework
- pyTelegramBotAPI / python-telegram-bot
- Git / GitHub

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/shibumi2906/florist.git
cd florist
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Tests

Run the test suite with:

```bash
python manage.py test
```

The repository contains basic Django tests for several application modules.

## Project Status

Educational portfolio project created to practice backend development with Django and implement a complete e-commerce flow:

**catalog → user → cart → order**

The Telegram integration is currently a prototype and requires refactoring of its configuration and database access before it can be considered fully portable.

## License

This project is distributed under the license provided in the `LICENSE` file.

---------------------------------------------------------------------------------






# Florist — Django Flower Shop

Веб-приложение интернет-магазина цветов на Django с каталогом товаров, регистрацией пользователей, оформлением заказов и экспериментальной интеграцией с Telegram-ботом.

Проект демонстрирует разработку классического серверного веб-приложения: работу с моделями и базой данных, пользовательской авторизацией, Django templates, сессиями, обработкой заказов и внешним интерфейсом через Telegram.

## Основные возможности

- просмотр каталога цветов;
- страницы отдельных товаров;
- регистрация и авторизация пользователей;
- добавление товаров в корзину;
- хранение корзины в пользовательской сессии;
- создание и просмотр заказов;
- управление товарами через Django Admin;
- загрузка и отображение изображений товаров;
- Telegram-бот для взаимодействия с каталогом и оформления заказа;
- базовые автоматические тесты Django.

## Архитектура

Приложение разделено на несколько Django-модулей:

```text
florist/
├── catalog/          # каталог товаров и работа с корзиной
├── orders/           # заказы пользователей
├── users/            # регистрация и работа с пользователями
├── flowershop/       # конфигурация Django-проекта
├── telegram_bot/     # Telegram-интерфейс
├── templates/        # HTML-шаблоны
├── static/           # CSS и статические ресурсы
├── media/            # изображения товаров
└── manage.py
```

### Catalog

Отвечает за хранение и отображение товаров. Для товара хранятся название, описание, цена и изображение.

Каталог позволяет получать список доступных позиций, открывать страницу товара и добавлять выбранные товары в корзину.

### Orders

Содержит модель заказа, связанную с пользователем и товаром.

Для заказа поддерживаются:

- количество товара;
- статус заказа;
- дата создания;
- связь с зарегистрированным пользователем.

### Users

Использует стандартную систему аутентификации Django и собственную форму регистрации пользователя с email.

### Telegram bot

В проекте также реализован прототип Telegram-интерфейса:

- команда `/start`;
- меню магазина;
- получение каталога;
- выбор товара;
- ввод адреса доставки;
- создание заказа.

Telegram-часть является экспериментальным модулем и требует дополнительной настройки перед использованием вне локальной среды.

## Технологии

- Python
- Django 4.2
- Django ORM
- SQLite
- Django Templates
- HTML / CSS
- Pillow
- Django REST Framework
- pyTelegramBotAPI / python-telegram-bot
- Git / GitHub

## Локальный запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/shibumi2906/florist.git
cd florist
```

### 2. Создать виртуальное окружение

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Выполнить миграции

```bash
python manage.py migrate
```

### 5. Создать администратора

```bash
python manage.py createsuperuser
```

### 6. Запустить сервер

```bash
python manage.py runserver
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Тесты

Запуск тестов:

```bash
python manage.py test
```

В репозитории присутствуют базовые Django-тесты для отдельных модулей проекта.

## Статус проекта

Учебный portfolio-проект, созданный для практики backend-разработки на Django и построения полного пользовательского сценария интернет-магазина: каталог → пользователь → корзина → заказ.

Telegram-интеграция находится на уровне прототипа и требует рефакторинга конфигурации и работы с базой данных для полноценного переносимого запуска.

## License

Проект распространяется на условиях лицензии, указанной в файле `LICENSE`.
