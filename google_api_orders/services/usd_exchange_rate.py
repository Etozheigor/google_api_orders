from datetime import date
from urllib.request import urlopen
from xml.etree import ElementTree


def get_usd_exchange_rate():
    """Функция для получения актуального курса USD на сегодняшнюю дату."""
    now_date = date.today().strftime('%d/%m/%Y')
    with urlopen(f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={now_date}") as xml:
        return (ElementTree.parse(xml).findtext('.//Valute[@ID="R01235"]/Value'))
