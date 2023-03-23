from sqlalchemy import Column, Date, Float, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Order(Base):
    """Модель заказа."""
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)
    order_number = Column(Integer, unique=True)
    price_usd = Column(Float)
    price_rub = Column(Float)
    delivery_date = Column(Date)

    def __repr__(self):
        return f'Заказ №{self.order_number}'
