from datetime import datetime

import schedule
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from db.create_db import PASSWORD, USER
from db.models import Base, Order
from services.google_api import (DRIVE_SERVICE, SHEETS_SERVICE, SPREADSHEET_ID,
                                 get_table_values, set_user_permissions)
from services.usd_exchange_rate import get_usd_exchange_rate

engine = create_engine(
    f'postgresql+psycopg2://{USER}:{PASSWORD}@localhost:5432/orders_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def clear_db(session):
    """Функция для удаления всех записей из базы данных."""
    session.query(Order).delete()


def add_orders_to_db(session, orders, usd_exchange_rate):
    """Функция для записи заказов в базу данных."""
    try:
        for order in orders[1:]:
            new_order = Order(
                number=order[0],
                order_number=order[1],
                price_usd=order[2],
                price_rub=round((float(order[2]) * usd_exchange_rate), 2),
                delivery_date=datetime.strptime(order[3], '%d.%m.%Y')
            )
            session.add(new_order)
        session.commit()
    except Exception:
        print('Ошибка записи данных в базу. Проверьте корректность исходных данных в гугл-таблице')


def update_db():
    """Функция для обновления данных в базе.
    Удаляем старые данные, выдаем права пользователю,
    получаем актуальный курс доллара, получаем список заказов из гугл-таблицы,
    записываем новые данные в базу.
    """
    clear_db(session)
    usd_exchange_rate = float(get_usd_exchange_rate().replace(',', '.'))
    set_user_permissions(DRIVE_SERVICE, SPREADSHEET_ID)
    orders_from_table = get_table_values(SHEETS_SERVICE)
    add_orders_to_db(session, orders_from_table, usd_exchange_rate)


def main():
    update_db()
    schedule.every(5).minutes.do(update_db)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
