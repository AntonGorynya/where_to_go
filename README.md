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
DEBUG=False
ALLOWED_HOSTS='*'
```
Вы можете сгенерировать ключ командой
```sh
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Как запустить
Для запуска сайта воспользуйтесь командой
```sh
python manage.py runserver
```
Для заполнения БД тестовыми данными воспользуйтесь командой
```python
python manage.py load_place 
```


### Пример сайта
Вы можете найти пример исполнения по ссылке
https://sdieul.pythonanywhere.com