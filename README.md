#  Проект Taski Docker

## Описание:

Проект для списка дел.
Ознакомиться с ним можно по адресу: [https://taskishmaski.ddns.net/](https://taskishmaski.ddns.net/)

## Технологии используемые в его создании и работе:

- Python
- Django
- React
- Nginx
- PostgreSQL
- Docker

## Для локального запуска в Docker контейнерах:

Необходимо предварительно установить:  
    - [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/)  
    или  
    - [Docker Desctop ](https://docs.docker.com/desktop/install/windows-install/)  
- В корневой папке проекта подготовить файл .env и наполнить по шаблону .env.example
- Запустить сборку и запуск контейнером командой
```
sudo docker compose up -d
```
По завершении работы команды фронтенд станет доступен по адресу [http://localhost:8000/](http://localhost:8000/) или [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
Для завершения подготовки бэкэнда необходимо:
- Выполнить миграции командой
```
sudo docker compose exec backend python manage.py migrate
```
- Подготовить статические файлы командой
```
sudo docker compose exec backend python manage.py collectstatic
```
- Cкопировать их в папку со статическими файлами, доступными nginx командой
```
sudo docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```
На этом процесс запуска проекта в Docker контейнерах локально завершен.