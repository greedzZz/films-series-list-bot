from bot import keyboards, states
from database import model as db_model
from logs import logged_execution
from user_interaction import texts


@logged_execution
def handle_start(message, bot, pool):
    current_user = db_model.get_user(pool, message.from_user.id)
    if not current_user:
        db_model.add_user(pool, message.from_user.id)
    bot.send_message(message.chat.id, texts.START, reply_markup=keyboards.EMPTY)


@logged_execution
def handle_add(message, bot, pool):
    current_user = db_model.get_user(pool, message.from_user.id)
    if not current_user:
        bot.send_message(message.chat.id, texts.NOT_STARTED, reply_markup=keyboards.EMPTY)
        return
    bot.send_message(message.chat.id, texts.ADD, reply_markup=keyboards.get_reply_keyboard(["/cancel"]))
    bot.set_state(message.from_user.id, states.AddState.name, message.chat.id)


@logged_execution
def handle_cancel_add(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, texts.ADD_CANCEL, reply_markup=keyboards.EMPTY)


@logged_execution
def handle_add_name(message, bot, pool):
    current_film = db_model.get_film(pool, message.from_user.id, message.text)
    if current_film:
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.send_message(message.chat.id, texts.EXISTS, reply_markup=keyboards.EMPTY)
        return
    bot.delete_state(message.from_user.id, message.chat.id)
    db_model.add_film(pool, message.from_user.id, message.text)
    bot.send_message(message.chat.id, texts.ADD_SUCCESS.format(message.text), reply_markup=keyboards.EMPTY)


@logged_execution
def handle_delete(message, bot, pool):
    current_user = db_model.get_user(pool, message.from_user.id)
    if not current_user:
        bot.send_message(message.chat.id, texts.NOT_STARTED, reply_markup=keyboards.EMPTY)
        return
    bot.send_message(message.chat.id, texts.DELETE, reply_markup=keyboards.get_reply_keyboard(["/cancel"]))
    bot.set_state(message.from_user.id, states.DeleteState.name, message.chat.id)


@logged_execution
def handle_cancel_delete(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, texts.DELETE_CANCEL, reply_markup=keyboards.EMPTY)


@logged_execution
def handle_delete_name(message, bot, pool):
    current_film = db_model.get_film(pool, message.from_user.id, message.text)
    if not current_film:
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.send_message(message.chat.id, texts.NOT_EXISTS, reply_markup=keyboards.EMPTY)
        return
    bot.delete_state(message.from_user.id, message.chat.id)
    db_model.delete_film(pool, message.from_user.id, message.text)
    bot.send_message(message.chat.id, texts.DELETE_SUCCESS.format(message.text), reply_markup=keyboards.EMPTY)


@logged_execution
def handle_update(message, bot, pool):
    current_user = db_model.get_user(pool, message.from_user.id)
    if not current_user:
        bot.send_message(message.chat.id, texts.NOT_STARTED, reply_markup=keyboards.EMPTY)
        return
    bot.send_message(message.chat.id, texts.UPDATE, reply_markup=keyboards.get_reply_keyboard(["/cancel"]))
    bot.set_state(message.from_user.id, states.UpdateState.name, message.chat.id)


@logged_execution
def handle_cancel_update(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, texts.UPDATE_CANCEL, reply_markup=keyboards.EMPTY)


@logged_execution
def handle_update_name(message, bot, pool):
    current_film = db_model.get_film(pool, message.from_user.id, message.text)
    if not current_film:
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.send_message(message.chat.id, texts.NOT_EXISTS, reply_markup=keyboards.EMPTY)
        return
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["name"] = message.text
    bot.set_state(message.from_user.id, states.UpdateState.select_field, message.chat.id)
    bot.send_message(message.chat.id, texts.UPDATE_CHOOSE.format(message.text),
                     reply_markup=keyboards.get_reply_keyboard(texts.UPDATE_LIST, ["/cancel"]))


@logged_execution
def handle_update_choose_field(message, bot, pool):
    if message.text not in texts.UPDATE_LIST:
        bot.send_message(message.chat.id,
                         texts.UPDATE_UNKNOWN.format(texts.UPDATE_LIST[0], texts.UPDATE_LIST[1],
                                                     texts.UPDATE_LIST[2], texts.UPDATE_LIST[3]),
                         reply_markup=keyboards.get_reply_keyboard(texts.UPDATE_LIST, ["/cancel"]))
        return

    bot.set_state(message.from_user.id, states.UpdateState.write_new_value, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["field"] = message.text
    if message.text == "type":
        bot.send_message(message.chat.id, texts.UPDATE_ENTER.format(message.text),
                         reply_markup=keyboards.get_reply_keyboard(texts.TYPE_LIST, ["/cancel"]))
    else:
        bot.send_message(message.chat.id, texts.UPDATE_ENTER.format(message.text),
                         reply_markup=keyboards.get_reply_keyboard(["/cancel"]))


@logged_execution
def handle_update_enter_value(message, bot, pool):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        field = data["field"]

    new_value = message.text
    if field == "type" and new_value not in texts.TYPE_LIST:
        bot.send_message(message.chat.id,
                         texts.WRONG_TYPE.format(texts.TYPE_LIST[0], texts.TYPE_LIST[1]),
                         reply_markup=keyboards.get_reply_keyboard(texts.TYPE_LIST, ["/cancel"]))
        return
    elif field == "year" and not new_value.isdigit():
        bot.send_message(message.chat.id, texts.WRONG_YEAR,
                         reply_markup=keyboards.get_reply_keyboard(["/cancel"]))
        return
    elif field == "year":
        new_value = int(new_value)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        name = data["name"]
    bot.delete_state(message.from_user.id, message.chat.id)
    current_film = db_model.get_film(pool, message.from_user.id, name)
    current_film[field] = new_value
    db_model.update_film(pool, **current_film)

    bot.send_message(message.chat.id, texts.UPDATE_SUCCESS.format(name), reply_markup=keyboards.EMPTY)


@logged_execution
def handle_show(message, bot, pool):
    current_user = db_model.get_user(pool, message.from_user.id)
    if not current_user:
        bot.send_message(message.chat.id, texts.NOT_STARTED, reply_markup=keyboards.EMPTY)
        return

    bot.send_message(message.chat.id, texts.SHOW_SORT,
                     reply_markup=keyboards.get_reply_keyboard(texts.SIMPLE_ANSWERS, ["/cancel"]))
    bot.set_state(message.from_user.id, states.ShowState.sort, message.chat.id)


@logged_execution
def handle_cancel_show(message, bot, pool):
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, texts.SHOW_CANCEL, reply_markup=keyboards.EMPTY)


@logged_execution
def handle_show_sort(message, bot, pool):
    if message.text not in texts.SIMPLE_ANSWERS:
        bot.send_message(message.chat.id,
                         texts.WRONG_SIMPLE_ANSWER.format(texts.SIMPLE_ANSWERS[0], texts.SIMPLE_ANSWERS[1]),
                         reply_markup=keyboards.get_reply_keyboard(texts.SIMPLE_ANSWERS, ["/cancel"]))
        return
    elif message.text == "да":
        bot.set_state(message.from_user.id, states.ShowState.select_sort_field, message.chat.id)
        bot.send_message(message.chat.id, texts.SHOW_SORT_CHOOSE,
                         reply_markup=keyboards.get_reply_keyboard(texts.SHOW_SORT_LIST, ["/cancel"]))
    elif message.text == "нет":
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["sort"] = message.text
        print_show_list(message, bot, pool)


@logged_execution
def handle_show_sort_choose_field(message, bot, pool):
    if message.text not in texts.SHOW_SORT_LIST:
        bot.send_message(message.chat.id,
                         texts.UPDATE_UNKNOWN.format(texts.SHOW_SORT_LIST[0], texts.SHOW_SORT_LIST[1],
                                                     texts.SHOW_SORT_LIST[2], texts.SHOW_SORT_LIST[3]),
                         reply_markup=keyboards.get_reply_keyboard(texts.SHOW_SORT_LIST, ["/cancel"]))
        return
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["sort"] = message.text
    print_show_list(message, bot, pool)


@logged_execution
def print_show_list(message, bot, pool):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        sort = data["sort"]

    current_list = None
    if sort == "нет":
        current_list = db_model.get_films(pool, message.from_user.id)
    else:
        if sort == "name":
            current_list = db_model.get_films_order_by_name(pool, message.from_user.id)
        elif sort == "type":
            current_list = db_model.get_films_order_by_type(pool, message.from_user.id)
        elif sort == "year":
            current_list = db_model.get_films_order_by_year(pool, message.from_user.id)
        elif sort == "country":
            current_list = db_model.get_films_order_by_country(pool, message.from_user.id)

    if len(current_list) == 0:
        bot.send_message(message.chat.id, texts.SHOW_EMPTY, reply_markup=keyboards.EMPTY)
    else:
        result = ""
        for film in current_list:
            result += "Название: {}\n".format(film["name"])
            result += "Тип: {}\n".format(film["type"]) if film["type"] else "Тип:\n"
            result += "Год: {}\n".format(film["year"]) if film["year"] else "Год:\n"
            result += "Страна: {}\n".format(film["country"]) if film["country"] else "Страна:\n"
            result += "Заметка: {}\n".format(film["note"]) if film["note"] else "Заметка:\n\n"
        bot.send_message(message.chat.id, texts.SHOW.format(result), reply_markup=keyboards.EMPTY)