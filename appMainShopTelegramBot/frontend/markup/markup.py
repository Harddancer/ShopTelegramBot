# импортируем специальные типы телеграм бота для создания элементов интерфейса
# импортируем класс-менеджер для работы с библиотекой
from db.database import get_db
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

# импортируем настройки и утилиты
from appMainShopTelegramBot.settings import config


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """

    # инициализация разметки

    def __init__(self):
        self.markup = None
        # инициализируем сессию  БД
        self.BD = get_db()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """

        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        """
        Создает разметку кнопок в основном меню и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn("CHOOSE_GOODS")
        itm_btn_2 = self.set_btn("INFO")
        itm_btn_3 = self.set_btn("SETTINGS")
        itm_btn_4 = self.set_btn("COMMENT")  # отзывы
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        self.markup.row(itm_btn_4)
        return self.markup
