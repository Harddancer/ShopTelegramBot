import logging

from db.database import get_db
from db.models import Product
from db.schemas import ProductSchema
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def create_product(obj: ProductSchema, db: Session = next(get_db())):
    """Создание товара в БД, проверяется уникальность названия товара

    Args:
        obj: информация о товаре
        db: сессия подключения к базе данных

    Returns:
        Результат добавления
    """
    # проверка существования товара
    product = db.query(Product).filter(Product.name == obj.name).first()
    if product:
        msg = "Товар с таким названием уже существует"
        return {"content": product, "msg_type": "w", "msg": msg}

    # создание объекта товара
    new_product = Product(
        name=obj.name,
        title=obj.title,
        price=obj.price,
        quantity=obj.quantity,
        is_active=obj.is_active,
        category_id=obj.category_id,
    )

    # создание записи в БД о товаре
    db.add(new_product)
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "e", "msg": msg}
    db.refresh(new_product)

    return {"content": new_product, "msg_type": "a", "msg": "Done"}


def get_product_by_id(product_id: int, db: Session = next(get_db())):
    """Получение товара из БД по id

    Args:
        product_id: id товара
        db: сессия подключения к базе данных

    Returns:
        Запись о товаре из БД
    """
    # получение товара
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        return {"content": product, "msg_type": "a", "msg": "Done"}
    else:
        msg = "Товара с таким id не существует"
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}


def get_product_by_category_id(category_id: int, db: Session = next(get_db())):
    """Получение товара из БД по category_id
        
    Args:
    category_id: id категории
    db: сессия подключения к базе данных

    Returns:
    Запись о товарах из БД согласно выбраной категории
    """    
    # получение всех товаров в категории
    product_by_category_id = db.query(Product).filter(Product.category_id == category_id).all()
    if product_by_category_id:
        return {"content": product_by_category_id, "msg_type": "a", "msg": "Done"}
    else:
        msg = "Товаров, относящихся к запрашиваемй категории не существует"
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}


def update_product(product_id: int, obj: ProductSchema, db: Session = next(get_db())):
    """Обновление товара в БД

    Args:
        product_id: id товара
        obj: информация о товаре
        db: сессия подключения к базе данных

    Returns:
        Результат обновления
    """

    # обновление товара по id
    db.query(Product).filter(Product.id == product_id).update(obj._asdict())
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "e", "msg": msg}

    updated_product = db.query(Product).filter(Product.id == product_id).first()
    return {"content": updated_product, "msg_type": "a", "msg": "Done"}


def delete_product(product_id: int, db: Session = next(get_db())):
    """Удаление товара из БД

    Args:
        product_id: id товара
        db: сессия подключения к базе данных

    Returns:
        Результат удаления
    """
    # получение объекта товара
    product = db.query(Product).filter(Product.id == product_id).first()
    db.delete(product)
    try:
        db.commit()
    except IntegrityError:
        msg = "Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}

    return {"content": [], "msg_type": "a", "msg": "Товар успешно удален"}
