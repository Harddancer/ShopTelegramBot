# импортируем класс родитель
from backend.handlers.handler import Handler

# импортируем сообщения пользователю
from settings.message import MESSAGES
from db.crud.orders_crud import create_order
from db.schemas import OrderSchema
from db.schemas import OrderProductSchema
from db.crud.products_crud import get_product_by_id
from db.crud.users_crud import create_user
from db.crud.users_crud import get_user_by_id
from db.crud.orders_products_crud import create_order_product
from db.crud.orders_products_crud import get_order_product_by_id
from db.crud.orders_crud import get_user_id_all_from_order, get_order_by_user_id
import datetime
from  settings.utility import convert



class HandlerInlineQuery(Handler):
    """
    Класс обрабатывает входящие текстовые
    сообщения от нажатия на инлайн-кнопоки
    """
    
    def __init__(self, bot):
        super().__init__(bot)
       
       

    def pressed_btn_product(self,call,productId:int,user:int):
        """
        Обрабатывает входящие запросы на нажатие inline-кнопок товара
        input params:
        call: объект события
        productId: id товара
        user: id пользователя
        """
        
        
        # получаем список всех product_id
        product_obj = get_product_by_id(productId)
        
        # требуется доработать валидацию пользователя
        user_bd = get_user_by_id(user)
        print(user_bd["content"])# пустой список тк нет ползователя в бд
        if user_bd["content"] == []:
            #требуется добавить create_user создание пользователя и заведенеи его в бд
            
            pass
        else:
            pass
        
        if user in convert(get_user_id_all_from_order()["content"]):
            order_id = get_order_by_user_id(user)
            product_obj = OrderProductSchema(product_obj["content"].id,order_id["content"].id)
            new_order = create_order_product(product_obj)
            product_from_db = get_order_product_by_id(new_order["content"].id)
            print("Есть такой пользователь с заказом")
            # ренедрим всплавающие меню при выборе товара
            self.bot.answer_callback_query(call.id, MESSAGES["product_order"].format(
                get_product_by_id(product_from_db["content"].product_id)["content"].title,
                get_product_by_id(product_from_db["content"].product_id)["content"].price,
                get_product_by_id(product_from_db["content"].product_id)["content"].quantity,
            show_alert=True))
        else:
            print("НЕТ такого пользователь с заказом")
            #Создаем объект для формирования заказа
            date = datetime.datetime.now()
            obj = OrderSchema(date,user)
            # создаем заказ
            order = create_order(obj)

            print(type(product_obj["content"].id))
            print(type(order["content"].id))
            # создаем экземпляр продукта
        product_obj = OrderProductSchema(product_obj["content"].id,order["content"].id)
        #добавляем продукт к заказу
        new_order = create_order_product(product_obj)
       # получем связку продукта и заказа
        product_from_db = get_order_product_by_id(new_order["content"].id)
        # print(product_from_db["content"].product_id)
        print("НЕТ такого пользователь с заказом###################")
        

        # ренедрим всплавающие меню при выборе товара
        self.bot.answer_callback_query(call.id, MESSAGES["product_order"].format(
            get_product_by_id(product_from_db["content"].product_id)["content"].title,
            get_product_by_id(product_from_db["content"].product_id)["content"].price,
            get_product_by_id(product_from_db["content"].product_id)["content"].quantity,
            show_alert=True))


        

    def handle(self):
        # обработчик(декоратор) запросов от нажатия на кнопки товара
        # для объекта bot  из бибилиотеке pyTelegramBotAPI
        #call.data - это InlineKeyboardButton(str(name)/
        #callback_data=str(name.id))
        # берем занчение  user_id
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            productId = call.data
            if productId.isdigit():
                productId = int(productId)
                user = call.from_user.id 
            self.pressed_btn_product(call, productId,user)