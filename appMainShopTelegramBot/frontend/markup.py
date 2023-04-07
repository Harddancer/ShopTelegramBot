from db.crud.products_crud import get_product_by_category_id
# импортируем настройки и утилиты
from settings import config
# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """

    # инициализация разметки

    def __init__(self):
        self.markup = None

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

    def info_menu(self):
        """
        Создает разметку кнопок в меню 'О магазине'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn("<<")
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn("<<")
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    @staticmethod
    def remove_menu():
        """
        Удаляет меню
        """
        return ReplyKeyboardRemove()

    def category_menu(self):
        """
        Создает разметку кнопок в меню категорий товара и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('EUROPEAN_MENU'))
        self.markup.add(self.set_btn('JAPANESE_MENU'))
        self.markup.add(self.set_btn('PIZZA'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    @staticmethod
    def set_inline_btn(name):
        """
        Создает и возвращает инлайн-кнопку по входным параметрам
        """
        return InlineKeyboardButton(str(name),
                                    callback_data=str(name.id))

    def set_select_category(self, category):
        """
        Создает разметку инлайн-кнопок в выбранной
        категории товара и возвращает разметку
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        # загружаем в названия инлайн-кнопок данные
        # из БД в соответствие с категорией товара
        list_product = get_product_by_category_id(category)["content"]
        for itm in list_product:
            self.markup.add(self.set_inline_btn(itm))
        return self.markup
    