import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение через .env postgres
# DATABASE_HOST = os.environ.get('DATABASE_HOST')
# DATABASE_PORT = os.environ.get('DATABASE_PORT')
# DATABASE_NAME = os.environ.get('DATABASE_NAME')
# DATABASE_USER = os.environ.get('DATABASE_USER')
# DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')

# url_object = URL.create(
#     'postgresql+psycopg2',
#     username=DATABASE_USER,
#     password=DATABASE_PASSWORD,
#     host=DATABASE_HOST,
#     port=DATABASE_PORT,
#     database=DATABASE_NAME
# )
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# для загрузки из env
load_dotenv()

SQLITE_NAME = os.environ.get("SQLITE_NAME")
engine = create_engine(f"sqlite:///{SQLITE_NAME}", future=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    """Создание сессии подключения к БД"""
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
        logging.error(f"Ошибка в подключении к базе данных")
