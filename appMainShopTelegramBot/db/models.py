from db.database import Base
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    """Таблица пользователей

    id: ID
    username: логин
    password: пароль в зашифрованном виде
    """

    # название таблицы
    __tablename__ = "users"

    # поля таблицы
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String)
    password = Column(String)

    # отношения
    answers = relationship(
        "Answer", back_populates=__tablename__, uselist=True, cascade="all, delete", passive_deletes=True
    )

    orders = relationship(
        "Order", back_populates=__tablename__, uselist=True, cascade="all, delete", passive_deletes=True
    )

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса
        """
        return f"< {self.username} >"


class BaseModel(Base):
    """Абстрактный класс, содержащий общие поля для всех таблиц

    id: идентификатор
    name: название/имя
    """

    # Абстрактная таблица для наследования
    __abstract__ = True

    # поля таблицы
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)


class Category(BaseModel):
    """
    Класс-модель для описания таблицы "Категория товара",
    основан на декларативном стиле SQLAlchemy
    """

    # название таблицы
    __tablename__ = "categories"

    # поля таблицы
    is_active = Column(Boolean)

    # отношения
    products = relationship(
        "Product", back_populates=__tablename__, uselist=True, cascade="all, delete", passive_deletes=True
    )

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса
        """
        return self.name


class Product(BaseModel):
    """
    Класс для создания таблицы "Товар",
    основан на декларативном стиле SQLAlchemy
    """

    # название таблицы
    __tablename__ = "products"

    # поля таблицы
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))

    # отношения
    categories = relationship("Category", back_populates=__tablename__)

    answers = relationship(
        "Answer", back_populates=__tablename__, uselist=True, cascade="all, delete", passive_deletes=True
    )

    orders_products = relationship(
        "OrderProduct", back_populates=__tablename__, uselist=True, cascade="all, delete", passive_deletes=True
    )

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса
        """
        return f"{self.name} {self.title} {self.price}"


class Answer(Base):
    """
    Класс для создания таблицы "Отзывы",
    основан на декларативном стиле SQLAlchemy
    """

    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text = Column(String)
    date = Column(Date)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    # отношения
    products = relationship("Product", back_populates=__tablename__)
    users = relationship("User", back_populates=__tablename__)

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса
        """
        return f"{self.name_product}{self.text}{self.user_id}"


class Order(Base):
    """
    Класс для создания таблицы "Заказ",
    основан на декларативном стиле SQLAlchemy
    """

    # название таблицы
    __tablename__ = "orders"

    # поля таблицы
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    # отношения
    users = relationship("User", back_populates=__tablename__)
    orders_products = relationship(
        "OrderProduct", back_populates=__tablename__, uselist=True, cascade="all, delete", passive_deletes=True
    )

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса
        """
        return f"{self.id} {self.date}"


class OrderProduct(Base):
    """
    Класс связей many2many для таблиц "Заказ" и "Товар"
    основан на декларативном стиле SQLAlchemy
    """

  
    __tablename__ = "orders_products"

    # поля таблицы
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))

    # отношения
    orders = relationship("Order", back_populates=__tablename__)
    products = relationship("Product", back_populates=__tablename__)

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса
        """
        return f"{self.product_id} - {self.order_id}"
