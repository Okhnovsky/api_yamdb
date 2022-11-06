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

### Пользовательские роли

- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django — обладает правами администратора (admin)

### Регистрация нового пользователя

Поля email и username должны быть уникальными.

Регистрация нового пользователя:

```
POST /api/v1/auth/signup/
```

```json
{
  "email": "string",
  "username": "string"
}
```

Получение JWT-токена:

```
POST /api/v1/auth/token/
```

```json
{
  "username": "string",
  "confirmation_code": "string"
}
```

### Примеры работы с API для авторизованных пользователей

Добавление категории:

```
Права доступа: Администратор.
POST /api/v1/categories/
```

```json
{
  "name": "string",
  "slug": "string"
}
```

Удаление категории:

```
Права доступа: Администратор.
DELETE /api/v1/categories/{slug}/
```

Добавление жанра:

```
Права доступа: Администратор.
POST /api/v1/genres/
```

```json
{
  "name": "string",
  "slug": "string"
}
```

Удаление жанра:

```
Права доступа: Администратор.
DELETE /api/v1/genres/{slug}/
```

Добавление пользователя:

```
Права доступа: Администратор
Поля email и username должны быть уникальными.
POST /api/v1/users/ - Добавление пользователя
```

```json
{
"username": "string",
"email": "user@example.com",
"first_name": "string",
"last_name": "string",
"bio": "string",
"role": "user"
}
```

Получение пользователя по username:

```
Права доступа: Администратор
GET /api/v1/users/{username}/ - Получение пользователя по username
```

Остальные примеры запросов и подробная документация доступна по эндпоинту /redoc/

Авторы проекта:
- [Александр Охновский](https://github.com/Okhnovsky)
- [Александр Ершов](https://github.com/rstaershov)
- [Александр Каунников](https://github.com/kaunnikov)
