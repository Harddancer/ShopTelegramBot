# импортируем библиотеку abc для реализации абстрактных классов
import abc

# импортируем бд
from db.database import get_db

# импортируем разметку клавиатуры и клавиш
from frontend.markup import Keyboards


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализируем разметку кнопок
        self.keybords = Keyboards()
        

    @abc.abstractmethod
    def handle(self):
        pass
