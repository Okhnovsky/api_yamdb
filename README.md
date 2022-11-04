### YaMDb - отзывы на произведения.
### О проекте
YaMDb позволяет пользователям оставлять отзывы к различного рода
произведениям: музыке, фильмам, книгам.

Однако сами произведения в YaMDb отсутствуют.

## Запуск проекта
- Клонируйте репозиторий.
- Установите и активируйте виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

- Установить зависимости из файла requirements.txt

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

- Выполнить миграции:

```bash
python manage.py migrate
```

Запускаем проект:

```bash
python manage.py runserver
```
