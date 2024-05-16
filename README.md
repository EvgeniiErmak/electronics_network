# Electronics Network

## Описание

Electronics Network - это веб-приложение для управления иерархической сетью по продаже электроники. Проект позволяет управлять объектами сети (заводы, розничные сети и индивидуальные предприниматели), отслеживать их задолженности и легко фильтровать данные через удобный интерфейс.

## Технические требования

- Python 3.8+
- Django 3+
- Django REST Framework (DRF) 3.10+
- PostgreSQL 10+

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/username/electronics_network.git
    cd electronics_network
    ```

2. Установите зависимости с помощью Poetry:

    ```sh
    poetry install
    ```

3. Создайте и настройте базу данных PostgreSQL.

4. Примените миграции:

    ```sh
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate
    ```

5. Создайте суперпользователя:

    ```sh
    poetry run python manage.py createsuperuser
    ```

6. Запустите сервер разработки:

    ```sh
    poetry run python manage.py runserver
    ```

## Функциональность

### Основные возможности

- Создание и управление объектами сети:
  - Завод
  - Розничная сеть
  - Индивидуальный предприниматель
- Отслеживание задолженности перед поставщиками
- Удобный интерфейс для фильтрации и поиска объектов
- Админ-панель для управления данными

### Админ-панель

- Вывод созданных объектов сети
- Ссылка на поставщика на странице объекта сети
- Фильтр по названию города
- Действие admin action для очистки задолженности перед поставщиком у выбранных объектов

### API

Используя Django REST Framework, реализованы следующие API-endpoints:

- CRUD для модели поставщика (запрещено обновление через API поля "Задолженность перед поставщиком")
- Фильтрация объектов по стране
- Доступ к API только для активных сотрудников

## Примеры использования

### Создание объекта сети через API

Для создания нового объекта сети через API, выполните POST запрос на `/api/nodes/` с телом запроса в формате JSON:

```json
{
  "name": "Retail Network",
  "email": "retail@example.com",
  "country": "USA",
  "city": "Los Angeles",
  "street": "Second",
  "house_number": "456",
  "product_name": "Product 2",
  "product_model": "Model Y",
  "product_release_date": "2024-01-01",
  "supplier": 1,
  "debt": 50.00
}
```

### Фильтрация объектов по стране через API

Для фильтрации объектов по стране, выполните GET запрос на `/api/nodes/?search=USA`.

### Очистка задолженности перед поставщиком

Для очистки задолженности перед поставщиком у выбранных объектов, выберите необходимые объекты в админ-панели и выполните действие "Очистить задолженность у выбранных узлов".

## Тестирование

Для запуска тестов выполните команду:

```sh
poetry run python manage.py test
```

## Структура проекта

```
electronics_network
├── electronics_network
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── network
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── templates
│   │   └── network
│   │       ├── base.html
│   │       ├── index.html
│   │       └── login.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── poetry.lock
├── pyproject.toml
└── templates
    └── network
        ├── base.html
        └── index.html
```

## Контакты

Если у вас есть вопросы или предложения, вы можете связаться с автором проекта:

- Имя: Евгений Ермак
- Телефон: +7 930-290-99-80
- Telegram: @DJErmak3000
- E-mail: ew.ermak5000@mail.ru
- GitHub: https://github.com/EvgeniiErmak

