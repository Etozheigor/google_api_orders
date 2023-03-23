import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient import discovery

load_dotenv()

CREDENTIALS_FILE = os.environ['CREDENTIALS_FILE']
SPREADSHEET_ID = os.environ['SPREADSHEET_ID']

SCOPES = [
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive',
]

CREDENTIALS = Credentials.from_service_account_file(
    filename=CREDENTIALS_FILE, scopes=SCOPES)

SHEETS_SERVICE = discovery.build('sheets', 'v4', credentials=CREDENTIALS)
DRIVE_SERVICE = discovery.build('drive', 'v3', credentials=CREDENTIALS)


def set_user_permissions(service, spreadsheetId):
    """Функция для выдчи прав пользователю для работы с документом."""
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': 'amkolotov@gmail.com'}
    service.permissions().create(
        fileId=spreadsheetId,
        body=permissions_body,
        fields='id'
    ).execute()


def get_table_values(service):
    """Функция для получения значений строк из таблицы.
    Каждая строка представлена в виде списка:
    Idx 0 - номер строки в списке заказов;
    Idx 1 - номер заказа;
    Idx 2 - цена в долларах;
    Idx 3 - срок поставки.
    """
    try:
        response = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range='Лист1'
        ).execute()
        return (response.get("values"))
    except Exception:
        print('Ошибка чтения данных из гугл-таблицы.')
