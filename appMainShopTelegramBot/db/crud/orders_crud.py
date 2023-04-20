import logging

from db.database import get_db
from db.models import Order
from db.schemas import OrderSchema
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def create_order(obj: OrderSchema, db: Session = next(get_db())):
    """Создание заказа в БД

    Args:
        obj: информация о заказе
        db: сессия подключения к базе данных

    Returns:
        Результат добавления
    """
    # создание объекта заказа
    new_order = Order(
        date=obj.date,
        user_id=obj.user_id,
    )

    # создание записи в БД о заказе
    db.add(new_order)
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "e", "msg": msg}
    db.refresh(new_order)

    return {"content": new_order, "msg_type": "a", "msg": "Done"}


def get_order_by_id(order_id: int, db: Session = next(get_db())):
    """Получение заказа из БД по id

    Args:
        order_id: id заказа
        db: сессия подключения к базе данных

    Returns:
        Запись о заказе из БД
    """
    # получение заказа
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        return {"content": order, "msg_type": "a", "msg": "Done"}
    else:
        msg = "Заказа с таким id не существует"
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}


def update_order(order_id: int, obj: OrderSchema, db: Session = next(get_db())):
    """Обновление заказа в БД

    Args:
        order_id: id заказа
        obj: информация о заказе
        db: сессия подключения к базе данных

    Returns:
        Результат обновления
    """

    # обновление заказа по id
    db.query(Order).filter(Order.id == order_id).update(obj._asdict())
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "e", "msg": msg}

    updated_order = db.query(Order).filter(Order.id == order_id).first()
    return {"content": updated_order, "msg_type": "a", "msg": "Done"}


def delete_order(order_id: int, db: Session = next(get_db())):
    """Удаление заказа из БД

    Args:
        order_id: id заказа
        db: сессия подключения к базе данных

    Returns:
        Результат удаления
    """
    # получение объекта заказа
    order = db.query(Order).filter(Order.id == order_id).first()
    db.delete(order)
    try:
        db.commit()
    except IntegrityError:
        msg = "Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}

    return {"content": [], "msg_type": "a", "msg": "Заказ успешно удален"}




