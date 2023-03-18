import os
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize
# импортируем модуль passslib для шифрования
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:
    """Клас шифрования и верификации
    """

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


# токен выдается при регистрации приложения
TOKEN = ''
# название БД
# NAME_DB = 'botshop.sqlite'
# версия приложения
VERSION = '1.0'
# автор приложния
AUTHOR = 'mvandron/kmoceiko'

# родительская директория до директории settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных 
# DB = "shopdb"
# DATABASE = os.path.join('sqlite:///'+BASE_DIR,DB,NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
