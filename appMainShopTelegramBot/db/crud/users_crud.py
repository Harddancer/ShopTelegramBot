import logging

from db.database import get_db
from db.models import User
from db.schemas import UserSchema
from settings import config
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def create_user(obj: UserSchema, db: Session = next(get_db())):
    """Создание пользователя в БД, проверяется уникальность логина

    Args:
        obj: информация о пользователе
        db: сессия подключения к базе данных

    Returns:
        Результат добавления
    """
    # проверка существования пользователя
    user = db.query(User).filter(User.username == obj.username).first()
    if user:
        msg = "Пользователь с таким именем уже существует"
        return {"content": user, "msg_type": "w", "msg": msg}

    # создание объекта пользователя
    new_user = User(username=obj.username, password=config.Hash.bcrypt(obj.password))

    # создание записи в БД о пользователе
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "e", "msg": msg}
    db.refresh(new_user)

    return {"content": new_user, "msg_type": "a", "msg": "Done"}


def get_user_by_id(user_id: int, db: Session = next(get_db())):
    """Получение пользователя из БД по id

    Args:
        user_id: id пользователя
        db: сессия подключения к базе данных

    Returns:
        Запись о пользователе из БД
    """
    # получение пользователя
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return {"content": user, "msg_type": "a", "msg": "Done"}
    else:
        msg = "Пользователя с таким id не существует"
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}


def update_user(user_id: int, obj: UserSchema, db: Session = next(get_db())):
    """Обновление пользователя в БД

    Args:
        user_id: id пользователя
        obj: информация о пользователе
        db: сессия подключения к базе данных

    Returns:
        Результат обновления
    """

    # обновление пользователя по id
    obj_dict = obj._asdict()
    obj_dict["password"] = config.Hash.bcrypt(obj.password)
    db.query(User).filter(User.id == user_id).update(obj_dict)
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "e", "msg": msg}

    updated_user = db.query(User).filter(User.id == user_id).first()
    return {"content": updated_user, "msg_type": "a", "msg": "Done"}


def delete_user(user_id: int, db: Session = next(get_db())):
    """Удаление пользователя из БД

    Args:
        user_id: id пользователя
        db: сессия подключения к базе данных

    Returns:
        Результат удаления
    """
    # получение объекта пользователя
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    try:
        db.commit()
    except IntegrityError:
        msg = "Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}

    return {"content": [], "msg_type": "a", "msg": "Пользователь успешно удален"}
