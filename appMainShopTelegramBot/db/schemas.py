import datetime
from typing import NamedTuple


class UserSchema(NamedTuple):
    """
    Класс для создания объекта пользователя
    """
    username: str
    password: str


class CategorySchema(NamedTuple):
    """
    Класс для создания объекта категории
    """
    name: str
    is_active: bool


class ProductSchema(NamedTuple):
    """
    Класс для создания объекта товара
    """
    name: str
    title: str
    price: float
    quantity: int
    is_active: bool
    category_id: int


class AnswerSchema(NamedTuple):
    """
    Класс для создания объекта отзыва
    """
    text: str
    date: datetime.date
    product_id: int
    user_id: int


class OrderSchema(NamedTuple):
    """
    Класс для создания объекта заказа
    """
    date: datetime.date
    user_id: int


class OrderProductSchema(NamedTuple):
    """
    Класс для создания объекта связи заказа и товара
    """
    product_id: int
    order_id: int
