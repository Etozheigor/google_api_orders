### Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Etozheigor/google_api_orders.git
```

```
cd google_api_orders
```

- Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

- Установить зависимости из файла requirements.txt (версии библиотек совместимы с Python версии 3.9):

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- создать файл .env и заполнить его по шаблону:

```
touch .env
```

шаблон заполнения файла:

```
POSTGRES_USER=*** # ваш логин для подключения к базе данных
POSTGRES_PASSWORD=*** # ваш пароль для подключения к БД
CREDENTIALS_FILE=your_file.json # название файла с данными вашего сервисного аккаунта гугл (см. пункт ниже)
SPREADSHEET_ID=*** # id документа, в котором будет обновляться таблица с заказами. (ID документа, с которым работал я: 1bmV22VtlbRoFEw2vocZaTn4TzC031auQDd05xdAllo0)
```

- Для работы с Google Spreadsheets необходимы данные сервисного аккаунта. Внутри папки с проектом необходимо перейти в папку google-api_orders и копировать туда json-файл с вашими данными. 
Если у вас нет нужного json файла, инструкцию по его получению можно найти, например, здесь: https://stackoverflow.com/questions/46287267/how-can-i-get-the-file-service-account-json-for-google-translate-api

- из главной директории проекта запустить базу данных Postgres (запускается в контейнере Docker):

```
docker-compose up
```

- перейти в папку приложения и создать базу данных:

```
cd google_api_orders
```
```
python db/create_db.py 
```

- запустить сам скрипт:

```
python main.py 
```

Каждые 5 минут скрипт будет считывать данные из таблицы и обновлять их в базе данных.


Ссылка на гугл-документ: https://docs.google.com/spreadsheets/d/1bmV22VtlbRoFEw2vocZaTn4TzC031auQDd05xdAllo0/edit#gid=0










