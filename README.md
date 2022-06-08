### О проекте:

Данный проект является классическим примером социальной сети с возможностями API.
В качестве фреймворка использовался Django 4.0.5.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Inozem/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Информация:


Аутентификация:
Аутентификация происходит способом отправки следующих HTTP-заголовков:
API-ключ, пример: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0Nzc5MDAwLCJqdGkiOiI3YjQ5MDg3ZTMwNjQ0OWNmODg0M2Y1NDJlYTM2YjBhNSIsInVzZXJfaWQiOjJ9.DSf7lLifm5joQeur7zbn5qis7uu6knJqBXvyHyfuYe0


Пример запроса получения постов:
GET http://127.0.0.1:8000/api/v1/posts/?limit=5&offset=3

Параметры:
limit - сколько постов выводить
offset - с какого поста начать

Пример ответа:
```
{
  "count": 7,
  "next": null,
  "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=5",
  "results": [
    {
      "id": 5,
      "text": "Пост юзера",
      "author": "user",
      "image": null,
      "group": null,
      "pub_date": "2022-06-06T15:37:40.160884Z"
    },
    {
      "id": 6,
      "text": "Пост юзера",
      "author": "user",
      "image": null,
      "group": null,
      "pub_date": "2022-06-06T15:37:40.473880Z"
    },
    {
      "id": 7,
      "text": "123",
      "author": "user",
      "image": null,
      "group": null,
      "pub_date": "2022-06-06T15:37:40.889064Z"
    },
    {
      "id": 8,
      "text": "Пост юзера",
      "author": "user",
      "image": null,
      "group": null,
      "pub_date": "2022-06-07T12:20:18.024394Z"
    }
  ]
}
```


Пример запроса публикации постов:
POST http://127.0.0.1:8000/api/v1/posts/

Пример ответа:
```
{
  "id": 9,
  "text": "123",
  "author": "user",
  "image": null,
  "group": null,
  "pub_date": "2022-06-08T17:04:08.040807Z"
}
```

Подробнее с примерами запросов можно ознакомиться по ссылке http://127.0.0.1:8000/redoc/ .

Автор проекта: Иноземцев Сергей