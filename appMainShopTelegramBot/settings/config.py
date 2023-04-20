# импортируем модуль logging для логирования
import logging
import logging.config
import os

from dotenv import load_dotenv

# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# импортируем модуль passslib для шифрования
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """Клас шифрования и верификации"""

    def bcrypt(self: str):
        """Метод, шифрующий строку

        Args:
             self: строка для шифрования

        Returns:
            зашифрованная строка
        """
        return pwd_cxt.hash(self)

    def verify(self: str, plain_password):
        """Метод, сравнивающий строку с зашифрованной строкой

        Args:
            self: зашифрованная строка
            plain_password: строка для сравнения

        Returns:
            True | False
        """
        return pwd_cxt.verify(plain_password, self)


load_dotenv()
# токен выдается при регистрации приложения
TOKEN = os.environ.get("TOKEN")
# название БД
# NAME_DB = 'botshop.sqlite'
# версия приложения
VERSION = os.environ.get("VERSION")
# автор приложния
AUTHOR = os.environ.get("AUTHOR")

# родительская директория до директории settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
# DB = "shopdb"
# DATABASE = os.path.join('sqlite:///'+BASE_DIR,DB,NAME_DB)

# для загрузки из env

COUNT = 0

# кнопки управления
KEYBOARD = {
    "CHOOSE_GOODS": emojize(":open_book: Меню"),
    "INFO": emojize(":speech_balloon: О кафе"),
    "SETTINGS": emojize("⚙️ Настройки"),
    "EUROPEAN_MENU": emojize(":fork_and_knife_with_plate: Европейское меню"),
    "JAPANESE_MENU": emojize(":chopsticks: Японское меню"),
    "PIZZA": emojize(":pizza: Пицца"),
    "<<": emojize("⏪ Вернуться назад"),
    ">>": emojize("⏩"),
    "BACK_STEP": emojize("◀️"),
    "NEXT_STEP": emojize("▶️"),
    "ORDER": emojize("✅ ЗАКАЗ"),
    "X": emojize("❌"),
    "DOUWN": emojize("🔽"),
    "AMOUNT_PRODUCT": COUNT,
    "AMOUNT_ORDERS": COUNT,
    "UP": emojize("🔼"),
    "APPLAY": "✅ Оформить заказ",
    "COMMENT": "✅ Отзывы о блюдах",
    "COPY": "©️",
}

# id категорий продуктов
CATEGORY = {
    "EUROPEAN_MENU": 1,
    "JAPANESE_MENU": 2,
    "PIZZA": 3,
}

# названия команд
COMMANDS = {
    "START": "start",
    "HELP": "help",
}

# Логирование
if not os.path.isdir("logs"):
    os.makedirs("logs")

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logging.conf")
logging.config.fileConfig(log_file_path)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("urllib3").propagate = False
logging.info(f"Конфигурация логов загружена")
