import logging

from db.database import get_db
from db.models import Answer
from db.schemas import AnswerSchema
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def create_answer(obj: AnswerSchema, db: Session = next(get_db())):
    """Создание отзыва в БД

    Args:
        obj: информация об отзыве
        db: сессия подключения к базе данных

    Returns:
        Результат добавления
    """

    # создание объекта отзыва
    new_answer = Answer(text=obj.text, date=obj.date, product_id=obj.product_id, user_id=obj.user_id)

    # создание записи в БД об отзыве
    db.add(new_answer)
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "e", "msg": msg}
    db.refresh(new_answer)

    return {"content": new_answer, "msg_type": "a", "msg": "Done"}


def get_answer_by_id(answer_id: int, db: Session = next(get_db())):
    """Получение отзыва из БД по id

    Args:
        answer_id: id отзыва
        db: сессия подключения к базе данных

    Returns:
        Запись об отзыве из БД
    """
    # получение отзыва
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if answer:
        return {"content": answer, "msg_type": "a", "msg": "Done"}
    else:
        msg = "Отзыва с таким id не существует"
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}


def update_answer(answer_id: int, obj: AnswerSchema, db: Session = next(get_db())):
    """Обновление отзыва в БД

    Args:
        answer_id: id отзыва
        obj: информация об отзыве
        db: сессия подключения к базе данных

    Returns:
        Результат обновления
    """

    # обновление отзыва по id
    db.query(Answer).filter(Answer.id == answer_id).update(obj._asdict())
    try:
        db.commit()
    except IntegrityError:
        msg = f"Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "e", "msg": msg}

    updated_answer = db.query(Answer).filter(Answer.id == answer_id).first()
    return {"content": updated_answer, "msg_type": "a", "msg": "Done"}


def delete_answer(answer_id: int, db: Session = next(get_db())):
    """Удаление отзыва из БД

    Args:
        answer_id: id отзыва
        db: сессия подключения к базе данных

    Returns:
        Результат удаления
    """
    # получение объекта отзыва
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    db.delete(answer)
    try:
        db.commit()
    except IntegrityError:
        msg = "Ошибка обработки данных."
        logging.warning(msg)
        return {"content": [], "msg_type": "w", "msg": msg}

    return {"content": [], "msg_type": "a", "msg": "Отзыв успешно удален"}
