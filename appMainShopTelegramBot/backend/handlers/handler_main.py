# импортируем класс HandlerCommands обработка комманд
# импортируем класс HandlerAllText -
# обработка нажатия на кнопки и иные сообщения
from backend.handlers.handler_all_text import HandlerAllText
from backend.handlers.handler_interface import HandlerCommands
from backend.handlers.handler_inline_query import HandlerInlineQuery


class HandlerMain:
    """
    Супер_класс
    """

    def __init__(self, bot):
        # получаем объект нашего бота
        self.bot = bot
        # здесь будет инициализация обработчиков
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)

    def handle(self):
        # здесь будет запуск обработчиков
        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_inline_query.handle()
