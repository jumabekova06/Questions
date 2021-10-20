# Questions

## Окружение проекта:
  * python 3.8
  * Django 2.2.10
  * djangorestframework

Склонируйте репозиторий с помощью git

    https://github.com/jumabekova06/Questions.git
Перейти в папку:
```bash
cd Questions
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:

```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/

* чтобы получить все возможные опросы http://127.0.0.1:8000/api/v1/survey/
* чтобы отправить ответ на опрос http://127.0.0.1:8000/v1answer
* чтобы получить вопросы http://127.0.0.1:8000/questions
