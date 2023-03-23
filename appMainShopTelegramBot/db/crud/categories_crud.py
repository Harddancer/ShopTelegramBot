from db.database import get_db
from db.models import Category
from db.schemas import CategorySchema
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def create_category(obj: CategorySchema, db: Session = next(get_db())):
    """Создание категории в БД, проверяется уникальность названия категории

    Args:
        obj: информация о категории
        db: сессия подключения к базе данных

    Returns:
        Результат добавления
    """
    # проверка существования категории
    category = db.query(Category).filter(Category.name == obj.name).first()
    if category:
        msg = "Категория с таким названием уже существует"
        return {"content": category, "msg_type": "w", "msg": msg}

    # создание объекта категории
    new_category = Category(name=obj.name, is_active=obj.is_active)

    # создание записи в БД о категории
    db.add(new_category)
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        return {"content": [], "msg_type": "e", "msg": msg}
    db.refresh(new_category)

    return {"content": new_category, "msg_type": "a", "msg": "Done"}


def get_category_by_id(category_id: int, db: Session = next(get_db())):
    """Получение категории из БД по id

    Args:
        category_id: id категории
        db: сессия подключения к базе данных

    Returns:
        Запись о категории из БД
    """
    # получение категории
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        return {"content": category, "msg_type": "a", "msg": "Done"}
    else:
        msg = "Категории с таким id не существует"
        return {"content": [], "msg_type": "w", "msg": msg}


def update_category(category_id: int, obj: CategorySchema, db: Session = next(get_db())):
    """Обновление категории в БД

    Args:
        category_id: id категории
        obj: информация о категории
        db: сессия подключения к базе данных

    Returns:
        Результат обновления
    """

    # обновление категории по id
    db.query(Category).filter(Category.id == category_id).update(obj._asdict())
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        return {"content": [], "msg_type": "e", "msg": msg}

    updated_category = db.query(Category).filter(Category.id == category_id).first()
    return {"content": updated_category, "msg_type": "a", "msg": "Done"}


def delete_category(category_id: int, db: Session = next(get_db())):
    """Удаление категории из БД

    Args:
        category_id: id категории
        db: сессия подключения к базе данных

    Returns:
        Результат удаления
    """
    # получение объекта категории
    category = db.query(Category).filter(Category.id == category_id).first()
    db.delete(category)
    try:
        db.commit()
    except IntegrityError:
        msg = "Ошибка обработки данных."
        return {"content": [], "msg_type": "w", "msg": msg}

    return {"content": [], "msg_type": "a", "msg": "Категория успешно удалена"}
