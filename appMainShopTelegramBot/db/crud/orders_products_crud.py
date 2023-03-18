from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import OrderProduct
from db.schemas import OrderProductSchema


def create_order_product(obj: OrderProductSchema, db: Session = next(get_db())):
    """Создание записи о товаре в заказе в БД

    Args:
        obj: информация о товаре в заказе
        db: сессия подключения к базе данных

    Returns:
        Результат добавления
    """
    # создание объекта записи о товаре в заказе
    new_order_product = OrderProduct(
        product_id=obj.product_id,
        order_id=obj.order_id
    )

    # создание записи в БД о товаре в заказе
    db.add(new_order_product)
    try:
        db.commit()
    except IntegrityError:
        msg = f'Ошибка обработки данных.'
        return {'content': [], 'msg_type': 'e', 'msg': msg}
    db.refresh(new_order_product)

    return {'content': new_order_product, 'msg_type': 'a', 'msg': 'Done'}


def get_order_product_by_id(order_product_id: int, db: Session = next(get_db())):
    """Получение записи о товаре в заказе из БД по id

    Args:
        order_product_id: id записи о товаре в заказе
        db: сессия подключения к базе данных

    Returns:
        Запись о товаре в заказе из БД
    """
    # получение записи о товаре в заказе
    order_product = db.query(OrderProduct).filter(OrderProduct.id == order_product_id).first()
    if order_product:
        return {'content': order_product, 'msg_type': 'a', 'msg': 'Done'}
    else:
        msg = 'Записи о товаре в заказе с таким id не существует'
        return {'content': [], 'msg_type': 'w', 'msg': msg}


def update_order_product(order_product_id: int, obj: OrderProductSchema, db: Session = next(get_db())):
    """Обновление записи о товаре в заказе в БД

    Args:
        order_product_id: id записи о товаре в заказе
        obj: информация о записи о товаре в заказе
        db: сессия подключения к базе данных

    Returns:
        Результат обновления
    """

    # обновление записи о товаре в заказе по id
    db.query(OrderProduct).filter(OrderProduct.id == order_product_id).update(obj._asdict())
    try:
        db.commit()
    except IntegrityError:
        msg = f'Ошибка обработки данных.'
        return {'content': [], 'msg_type': 'e', 'msg': msg}

    updated_order_product = db.query(OrderProduct).filter(OrderProduct.id == order_product_id).first()
    return {'content': updated_order_product, 'msg_type': 'a', 'msg': 'Done'}


def delete_order_product(order_product_id: int, db: Session = next(get_db())):
    """Удаление записи о товаре в заказе из БД

    Args:
        order_product_id: id записи о товаре в заказе
        db: сессия подключения к базе данных

    Returns:
        Результат удаления
    """
    # получение объекта записи о товаре в заказе
    order_product = db.query(OrderProduct).filter(OrderProduct.id == order_product_id).first()
    db.delete(order_product)
    try:
        db.commit()
    except IntegrityError:
        msg = 'Ошибка обработки данных.'
        return {'content': [], 'msg_type': 'w', 'msg': msg}

    return {'content': [], 'msg_type': 'a', 'msg': 'Товар успешно удален'}
