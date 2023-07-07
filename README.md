# Where to go
Данный репозиторий представляет собой интерактивную карту Москвы, на которой будут отмечены все известные виды активного отдыха с подробными описаниями и комментариями

### Как установить
Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
Создайте суперпользователя
```sh
python3 manage.py createsuperuser
```

Перед установкой создайте файл **.env** в папке **where_to_go** вида:
```properties
SECRET_KEY='ваш ключ'
```


### Как запустить
Для запуска сайта воспользуйтесь командой
```sh
python manage.py runserver
```
