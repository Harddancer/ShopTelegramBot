# импортируем класс родитель
from backend.handlers.handler import Handler


class HandlerCommands(Handler):
    """
    Класс обрабатывает входящие команды /start и /help и т.п.
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        """
        обрабатывает входящие /start команды
        """
        self.bot.send_message(
            message.chat.id,
            f"{message.from_user.first_name}," f" Приветствую, я бот-Alice, помогу Вам в оформлении заказа!",
            # self.keybords.start_menu()- берем из класса родителя Handler.
            reply_markup=self.keybords.start_menu(),
        )

    def handle(self):
        # обработчик(декоратор) сообщений,

        @self.bot.message_handler(commands=["start"])
        def handle(message):
            if message.text == "/start":
                self.pressed_btn_start(message)
