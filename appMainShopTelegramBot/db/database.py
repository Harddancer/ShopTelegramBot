import os

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение через .env postgres
# DATABASE_LIB = os.environ.get('DB_CONNECT_LIB')
# DATABASE_CONNECT_TYPE = os.environ.get('DB_CONNECT_TYPE')
# DATABASE_HOST = os.environ.get('DB_CONNECT_IP')
# DATABASE_PORT = os.environ.get('DB_CONNECT_PORT')
# DATABASE_NAME = os.environ.get('DB_CONNECT_NAME')
# DATABASE_USER = os.environ.get('DB_CONNECT_USER')
# DATABASE_PASSWORD = os.environ.get('DB_CONNECT_PSWD')

# SQLALCHEMY_DATABASE_URL = f'{DATABASE_CONNECT_TYPE}+{DATABASE_LIB}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine("sqlite:///botshop.db")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    """Создание сессии подключения к БД
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_db():
    from db.models import Base
    try:
        Base.metadata.create_all(engine)
    except OperationalError:
        print(f'Ошибка в подключении к базе данных')


if __name__ == '__main__':
    create_db()

    # from db.crud.users_crud import create_user, get_user_by_id, update_user, delete_user
    # from db.schemas import UserSchema
    #
    # # test_1
    # _new_user = UserSchema(username='testuser', password='testpassword')
    # print(f'CREATE:\n{create_user(_new_user)}')
    #
    # # test_2
    # _user_id = 1
    # print(f'READ:\n{get_user_by_id(_user_id)}')
    #
    # # test_3
    # _updated_user = UserSchema(username='testuser', password='testpassword2')
    # print(f'UPDATE:\n{update_user(_user_id, _updated_user)}')
    #
    # # test_4
    # print(f'UPDATE:\n{delete_user(_user_id)}')
