from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey,func
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import Enum as SAEnum
from enum import Enum
import datetime
from sqlalchemy import Index, Column, Date, DateTime, func

from fastapi import FastAPI

# строка подключения
SQLALCHEMY_DATABASE_URL = "postgresql://admin:root@localhost:5433/postgres_flow"

# создаем движок SqlAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#создаем базовый класс для моделей
Base = declarative_base()

# создаем модель, объекты которой будут храниться в бд
# Определяем модели для таблиц
class OrderStatus(Enum):
    RESERVED = 'Reserved'
    PROCESSING = 'Processing'
    ASSEMBLING = 'Assembling'
    IN_TRANSIT = 'In transit'
    RECEIVED = 'Received'

class PackagingStatus(Enum):
    RESERVED = 'Reserved'
    ASSEMBLING = 'Assembling'
    ASSEMBLED = 'Assembled'

class DeliveryStatus(Enum):
    RESERVED = 'Reserved'
    IN_TRANSIT = 'In Transit'
    RECEIVED = 'Received'

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    fio = Column(String(60), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=True, unique=True)
    birth_date = Column(Date, nullable=False)
    email = Column(String(100), nullable=True)

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    fio = Column(String(60), nullable=False, unique=True)
    position = Column(String(40), nullable=True)
    phone = Column(String(20), nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)
    address = Column(String(100), nullable=True)

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    reserve_end_date = Column(Date, nullable=True)
    status = Column(SAEnum(PackagingStatus), nullable=True, default=PackagingStatus.RESERVED)
    employee = relationship("Employee", back_populates="orders")
    client = relationship("Client", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    update_date = Column(DateTime, nullable=True)

class OrderProduct(Base):
    __tablename__ = "order_product"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    deletion_date = Column(DateTime, nullable=True)

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(50), nullable=False)
    color = Column(String(35), nullable=True)
    stock_quantity = Column(Integer, nullable=False, default=0)
    price = Column(Float, nullable=False, default=0.00)
    length = Column(Float, nullable=False, default=0.0)
    orders = relationship("Order", secondary="order_product")
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    deletion_date = Column(DateTime, nullable=True)

class Supply(Base):
    __tablename__ = "supply"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    price = Column(Float, nullable=False, default=0.00)
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    deletion_date = Column(DateTime, nullable=True)

class SupplyProduct(Base):
    __tablename__ = "supply_product"
    id = Column(Integer, ForeignKey('supply.id'), primary_key=True, unique=True)
    supply_id = Column(Integer, ForeignKey('supply.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    deletion_date = Column(DateTime, nullable=True)

class Packaging(Base):
    __tablename__ = "packaging"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    order_id = Column(Integer, ForeignKey('order.id'))
    status = Column(SAEnum(PackagingStatus), nullable=True, default=PackagingStatus.RESERVED)
    employee = relationship("Employee", back_populates="packaging")
    order = relationship("Order", back_populates="packaging")
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    deletion_date = Column(DateTime, nullable=True)

class Delivery(Base):
    __tablename__ = "delivery"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    address = Column(String(100), nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    price = Column(Float, nullable=False, default=0.00)
    status = Column(SAEnum(DeliveryStatus), nullable=True, default=DeliveryStatus.RESERVED)
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    deletion_date = Column(DateTime, nullable=True)

class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    notification_type = Column(String(14), nullable=True)
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    deletion_date = Column(DateTime, nullable=True)

class Receipt(Base):
    __tablename__ = "receipt"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    total_amount = Column(Float, nullable=False, default=0.00)
    creation_date = Column(DateTime, nullable=False, default=func.current_timestamp())

# Создаем индексы
Index('idx_order_employee_id', Order.employee_id)
Index('idx_order_client_id', Order.client_id)
Index('idx_order_product_id', Order.product_id)

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# приложение, которое ничего не делает
app = FastAPI()