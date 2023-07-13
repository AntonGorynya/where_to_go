# Where to go
Данный репозиторий представляет собой интерактивную карту Москвы, на которой будут отмечены все известные виды активного отдыха с подробными описаниями и комментариями

### Как установить
Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```
Перед установкой создайте файл **.env** в папке **where_to_go** вида:
```properties
SECRET_KEY='ваш ключ'
DEBUG=False
ALLOWED_HOSTS=.example.com,127.0.0.1
STATIC_ROOT='./web_app/static'
```
Вы можете сгенерировать ключ командой
```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Создайте базу данных SQLite

```sh
python manage.py migrate
```
Создайте суперпользователя
```sh
python manage.py createsuperuser
```

### Как запустить
Для запуска сайта воспользуйтесь командой
```sh
python manage.py runserver
```
Для заполнения БД тестовыми данными воспользуйтесь командой
```sh
python manage.py load_place 
```
Для загрузки собственных данных введите команду ввида
```sh
python manage.py load_place https://mydata.url/master.zip
```
По умолчанию скрипт скачивает архив данных с [репозитария](
https://github.com/devmanorg/where-to-go-places/
) на гитхабе. Важно, что бы в иных ссылках сохранялась структура репозитория.

### Пример сайта
Вы можете найти пример исполнения по ссылке
https://sdieul.pythonanywhere.com