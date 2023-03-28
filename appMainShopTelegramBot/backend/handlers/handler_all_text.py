# импортируем ответ пользователю
# импортируем класс-родитель
from backend.handlers.handler import Handler
from settings import config
from settings.message import MESSAGES


class HandlerAllText(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)
        self.step = 0

    def pressed_btn_info(self, message):
        """
        Обработчик кнопочки 'О магазине'
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

    def pressed_btn_back(self, message):
        """
        обрабатывает входящие текстовые сообщения от нажатия на кнопку 'Назад'.
        """
        self.bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=self.keybords.start_menu())

    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # ********** меню ********** #

            if message.text == config.KEYBOARD["INFO"]:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD["SETTINGS"]:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD["<<"]:
                self.pressed_btn_back(message)
