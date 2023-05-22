# импортируем класс-родитель
from backend.handlers.handler import Handler
from settings import config
# импортируем ответ пользователю
from settings.message import MESSAGES
from db.crud.answers_crud import get_answer_all
from db.crud.orders_crud import get_order_by_user_id
from db.crud.orders_products_crud import get_product_all_from_order

class HandlerAllText(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)
        self.step = 0
    
    def pressed_btn_category(self, message):
        """
        Обработка события нажатия на кнопку 'Меню'. А точнее
        это выбор категории товаров
        """
        self.bot.send_message(message.chat.id, "Меню",
                              reply_markup=self.keybords.remove_menu())
        self.bot.send_message(message.chat.id, "Сделайте свой выбор",
                              reply_markup=self.keybords.category_menu())

    def pressed_btn_info(self, message):
        """
        Обработчик кнопочки 'О кафе'
        """
        self.bot.send_message(
            message.chat.id, MESSAGES["trading_store"], parse_mode="HTML", reply_markup=self.keybords.info_menu()
        )

    def pressed_btn_settings(self, message):
        """
        Обработчик кнопочки 'Настройки'
        """
        self.bot.send_message(
            message.chat.id, MESSAGES["settings"], parse_mode="HTML", reply_markup=self.keybords.settings_menu()
        )
    
    def pressed_btn_comment(self, message):
        """
        Обработчик кнопочки 'Отзывы о блюдах'
        """
        answer_all=get_answer_all()["content"]

        self.bot.send_message(message.chat.id, "👇 Отзывы на наши блюда и напитки 😋",
                              reply_markup=self.keybords.comment_menu())
        for itm in answer_all:
            self.bot.send_message(message.chat.id, 
                                MESSAGES["comment"].
                                format(itm[0], itm[1]), parse_mode="HTML")
        
    def pressed_btn_back(self, message):
        """
        обрабатывает входящие текстовые сообщения от нажатия на кнопку 'Назад'.
        """
        self.bot.send_message(message.chat.id, "👇 Вы вернулись в главное меню", 
                              reply_markup=self.keybords.start_menu())

    def pressed_btn_product(self, message, product):
        """
        Обработка события нажатия на кнопку 'Выбрать товар'. А точнее
        это выбор товара из категории
        """
        self.bot.send_message(message.chat.id, 'Категория ' +
                              config.KEYBOARD[product],
                              reply_markup=self.keybords.set_select_category(config.CATEGORY[product]))
        self.bot.send_message(message.chat.id, "Ок",
                              reply_markup=self.keybords.category_menu())
    
    def pressed_btn_order(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопку 'Заказ'.
        """
        order_id = get_order_by_user_id(message.from_user.id)
        # получаем список всех товаров в заказе
        print("###################")
        products = get_product_all_from_order(order_id)["content"]
        # отправляем ответ пользователю
       
        for itm in products:
            self.bot.send_message(message.chat.id,
                      MESSAGES['order'].format(itm[0], itm[1],itm[2],itm[3],itm[4]), parse_mode="HTML")




    
    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # ********** меню ********** #
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD["INFO"]:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD["SETTINGS"]:
                self.pressed_btn_settings(message)
            
            if message.text == config.KEYBOARD["COMMENT"]:
                self.pressed_btn_comment(message)

            if message.text == config.KEYBOARD["<<"]:
                self.pressed_btn_back(message)

            # ********** меню (категории товара, ПФ, Бакалея, Мороженое)******
            if message.text == config.KEYBOARD['EUROPEAN_MENU']:
                self.pressed_btn_product(message, 'EUROPEAN_MENU')

            if message.text == config.KEYBOARD['JAPANESE_MENU']:
                self.pressed_btn_product(message, 'JAPANESE_MENU')

            if message.text == config.KEYBOARD['PIZZA']:
                self.pressed_btn_product(message, 'PIZZA')

            if message.text == config.KEYBOARD['ORDER']:
                user_id = message.from_user.id
                
                if get_order_by_user_id(user_id)["content"].id > 0:
                    
                    self.pressed_btn_order(message)
                else:
                    self.bot.send_message(message.chat.id,MESSAGES['no_orders'],
                        parse_mode="HTML",
                        reply_markup=self.keybords.category_menu())
