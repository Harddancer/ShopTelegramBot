# импортируем настройки для отражения эмоджи
from .config import AUTHOR, KEYBOARD, VERSION
from db.crud.answers_crud import get_answer_all


# ответ пользователю при посещении блока "О магазине"
trading_store = """
<b>Добро пожаловать в телеграм-бот Есенин!</b>

Данное приложение разработано специально для Вас, дорогие гости!
При помощи бота Вы можете ознакомиться с меню, 
заказать блюдо, напиток, почитать отзывы.

«Есенин» – это семейное место? Место для громких вечеринок? Или, быть может, для банкетов? Каждое из утверждений будет верным. Ведь «Есенин» – это, прежде всего, место, где ценят каждого гостя, его предпочтения и вкусы, привычки и желание получить максимум положительных эмоций. Кафе лаунж «Есенин» – это место, созданное вашей любовью к хорошему отдыху.
И Вам всегда здесь рады! 
"""

# ответ пользователю при посещении блока "Настройки"
settings = """
<b>Общее руководство приложением:</b>

<i>Навигация:</i>

<b>{} - </b><i>назад в главное меню</i>
<b>{} - </b><i>вперед</i>
<b>{} - </b><i>увеличить</i>
<b>{} - </b><i>уменьшить</i>
<b>{} - </b><i>следующий</i>
<b>{} - </b><i>предыдующий</i>

<i>Специальные кнопки:</i>

<b>{} - </b><i>удалить</i>
<b>{} - </b><i>заказ</i>
<b>{} - </b><i>Оформить заказ</i>


<b>{}Есенин original trademark</b>
<b>{}BugsUp software engineering group</b>
<b>Latest version:</b><i> {}</i>
""".format(
    KEYBOARD["<<"],
    KEYBOARD[">>"],
    KEYBOARD["UP"],
    KEYBOARD["DOUWN"],
    KEYBOARD["NEXT_STEP"],
    KEYBOARD["BACK_STEP"],
    KEYBOARD["X"],
    KEYBOARD["ORDER"],
    KEYBOARD["APPLAY"],
    KEYBOARD["COPY"],
    KEYBOARD["COPY"],
    VERSION,
)

# ответ пользователю при посещении блока "Отзывыв о блюдах"
comment = """
<b>Блюдо: {}</b>

<b>Отзыв о блюде:</b>
<i>{}</i>
"""

# ответ пользователю при добавлении товара в заказ
product_order = """
Выбранный товар:

{}
{}
Cтоимость: {} руб

добавлен в заказ!

На складе осталось {} ед. 
"""

# ответ пользователю при посещении блока с заказом
order = """

<i>Название:</i> <b>{}</b>

<i>Описание:</i> <b>{}</b>

<i>Cтоимость:</i> <b>{} руб за 1 ед.</b>

<i>Количество позиций:</i> <b>{} ед.</b> 
"""

order_number = """

<b>Позиция в заказе № </b> <i>{}</i>

"""

# ответ пользователю, когда заказа нет
no_orders = """
<b>Заказ отсутствует !</b>
"""

# ответ пользователю при подтверждении оформления заказа
applay = """
<b>Ваш заказ оформлен !</b>

<i>Общая стоимость заказа составляет:</i> <b>{} руб</b>

<i>Общее количество позиций составляет:</i> <b>{} ед.</b>

<b>ЗАКАЗ НАПРАВЛЕН НА СКЛАД,
ДЛЯ ЕГО КОМПЛЕКТОВКИ !</b>
"""

# словарь ответов пользователю
MESSAGES = {
    "trading_store": trading_store,
    "comment": comment,
    "product_order": product_order,
    "order": order,
    "order_number": order_number,
    "no_orders": no_orders,
    "applay": applay,
    "settings": settings,
}
