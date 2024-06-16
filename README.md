# TG BOT

## Реализованная функциональность

* Квизы
* Отправка фоток в Kafka
* Cохранение/ отдача фоток из s3
* docker_compose

## Стек
### Backend
* Python,
* PostgreSQL, SQLAlchemy
* Faststream
* Pydantic
* aiogram
* Docker, Docker-compose

## Как развернуть:
###   из докера весь сервис:
1. Клонируем
```bash
foo@bar:~$ git clone https://github.com/AtomHackPaws/TG_Service
```
2. Заходим в папку
```bash
foo@bar:~$ cd TG_Service
```
3. Настройте файл .env для запуска
```bash
    foo@bar:~$ vim .env
  POSTGRES_DATABASE=db_name
  POSTGRES_USER=db_user
  POSTGRES_PASSWORD=db_pass
  MINIO_ROOT_USER=minio_user
  MINIO_ROOT_PASSWORD=minio_pass
  MINIO_BUCKET=minio-bucket
  TELEGRAM_BOT_TOKEN=<YOUR TOKEN>
  CHANNEL_ID=<YOUR CHANNEL_ID>
  MINIO_LINK=http://s3storage:9200
  KAFKA_URL=kafka:9093
  KAFKA_SERVER=kafka
```
4. Cоздаем сеть
```bash
foo@bar:~$ docker network create atom-dev
```
5. Запускаем докер
```bash
foo@bar:~$ docker-compose up
```
###   локально при условии что все сервисы запущены:
1. Клонируем
```bash
foo@bar:~$ git clone https://github.com/AtomHackPaws/TG_Service
```
2. Заходим в папку
```bash
foo@bar:~$ cd TG_Service
```
3. Настройте файл .env для запуска
```bash
    foo@bar:~$ vim .env
  POSTGRES_DATABASE=db_name
  POSTGRES_USER=db_user
  POSTGRES_PASSWORD=db_pass
  MINIO_ROOT_USER=minio_user
  MINIO_ROOT_PASSWORD=minio_pass
  MINIO_BUCKET=minio-bucket
  TELEGRAM_BOT_TOKEN=<YOUR TOKEN>
  CHANNEL_ID=<YOUR CHANNEL_ID>
  MINIO_LINK=http://s3storage:9200
  KAFKA_URL=kafka:9093
  KAFKA_SERVER=kafka
```
4. Иницилизируем и запускаем .venv
```bash
foo@bar:~$ poetry install
```
5. Запускаем бота
```bash
foo@bar:~$ python main.py
```

## Где посомтреть работу:
https://t.me/toni_atom_bot
