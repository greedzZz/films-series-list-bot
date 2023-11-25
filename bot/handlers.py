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
        bot.send_message(message.chat.id, texts.ADD_EXISTS, reply_markup=keyboards.EMPTY)
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
        bot.send_message(message.chat.id, texts.DELETE_NOT_EXISTS, reply_markup=keyboards.EMPTY)
        return
    bot.delete_state(message.from_user.id, message.chat.id)
    db_model.delete_film(pool, message.from_user.id, message.text)
    bot.send_message(message.chat.id, texts.DELETE_SUCCESS.format(message.text), reply_markup=keyboards.EMPTY)


# @logged_execution
# def handle_start(message, bot, pool):
#     bot.send_message(message.chat.id, texts.START, reply_markup=keyboards.EMPTY)
#
#
# @logged_execution
# def handle_register(message, bot, pool):
#     current_data = db_model.get_user_info(pool, message.from_user.id)
#
#     if current_data:
#         bot.send_message(
#             message.chat.id,
#             texts.ALREADY_REGISTERED.format(
#                 current_data["first_name"],
#                 current_data["last_name"],
#                 current_data["age"],
#             ),
#             reply_markup=keyboards.EMPTY,
#         )
#         return
#
#     bot.send_message(
#         message.chat.id,
#         texts.FIRST_NAME,
#         reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
#     )
#     bot.set_state(
#         message.from_user.id, states.RegisterState.first_name, message.chat.id
#     )
#
#
# @logged_execution
# def handle_cancel_registration(message, bot, pool):
#     bot.delete_state(message.from_user.id, message.chat.id)
#     bot.send_message(
#         message.chat.id,
#         texts.CANCEL_REGISTER,
#         reply_markup=keyboards.EMPTY,
#     )
#
#
# @logged_execution
# def handle_get_first_name(message, bot, pool):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data["first_name"] = message.text
#     bot.set_state(message.from_user.id, states.RegisterState.last_name, message.chat.id)
#     bot.send_message(
#         message.chat.id,
#         texts.LAST_NAME,
#         reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
#     )
#
#
# @logged_execution
# def handle_get_last_name(message, bot, pool):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data["last_name"] = message.text
#     bot.set_state(message.from_user.id, states.RegisterState.age, message.chat.id)
#     bot.send_message(
#         message.chat.id,
#         texts.AGE,
#         reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
#     )
#
#
# @logged_execution
# def handle_get_age(message, bot, pool):
#     if not message.text.isdigit():
#         bot.send_message(
#             message.chat.id,
#             texts.AGE_IS_NOT_NUMBER,
#             reply_markup=keyboards.EMPTY,
#         )
#         return
#
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         first_name = data["first_name"]
#         last_name = data["last_name"]
#         age = int(message.text)
#
#     bot.delete_state(message.from_user.id, message.chat.id)
#     db_model.add_user_info(pool, message.from_user.id, first_name, last_name, age)
#
#     bot.send_message(
#         message.chat.id,
#         texts.DATA_IS_SAVED.format(first_name, last_name, age),
#         reply_markup=keyboards.EMPTY,
#     )
#
#
# @logged_execution
# def handle_show_data(message, bot, pool):
#     current_data = db_model.get_user_info(pool, message.from_user.id)
#
#     if not current_data:
#         bot.send_message(
#             message.chat.id, texts.NOT_REGISTERED, reply_markup=keyboards.EMPTY
#         )
#         return
#
#     bot.send_message(
#         message.chat.id,
#         texts.SHOW_DATA_WITH_PREFIX.format(
#             current_data["first_name"], current_data["last_name"], current_data["age"]
#         ),
#         reply_markup=keyboards.EMPTY,
#     )
#
#
# @logged_execution
# def handle_delete_account(message, bot, pool):
#     current_data = db_model.get_user_info(pool, message.from_user.id)
#     if not current_data:
#         bot.send_message(
#             message.chat.id, texts.NOT_REGISTERED, reply_markup=keyboards.EMPTY
#         )
#         return
#
#     bot.send_message(
#         message.chat.id,
#         texts.DELETE_ACCOUNT,
#         reply_markup=keyboards.get_reply_keyboard(texts.DELETE_ACCOUNT_OPTIONS),
#     )
#     bot.set_state(
#         message.from_user.id, states.DeleteAccountState.are_you_sure, message.chat.id
#     )
#
#
# @logged_execution
# def handle_finish_delete_account(message, bot, pool):
#     bot.delete_state(message.from_user.id, message.chat.id)
#
#     if message.text not in texts.DELETE_ACCOUNT_OPTIONS:
#         bot.send_message(
#             message.chat.id,
#             texts.DELETE_ACCOUNT_UNKNOWN,
#             reply_markup=keyboards.EMPTY,
#         )
#         return
#
#     if texts.DELETE_ACCOUNT_OPTIONS[message.text]:
#         db_model.delete_user_info(pool, message.from_user.id)
#         bot.send_message(
#             message.chat.id,
#             texts.DELETE_ACCOUNT_DONE,
#             reply_markup=keyboards.EMPTY,
#         )
#     else:
#         bot.send_message(
#             message.chat.id,
#             texts.DELETE_ACCOUNT_CANCEL,
#             reply_markup=keyboards.EMPTY,
#         )
#
#
# @logged_execution
# def handle_change_data(message, bot, pool):
#     current_data = db_model.get_user_info(pool, message.from_user.id)
#
#     if not current_data:
#         bot.send_message(
#             message.chat.id, texts.NOT_REGISTERED, reply_markup=keyboards.EMPTY
#         )
#         return
#
#     bot.set_state(
#         message.from_user.id, states.ChangeDataState.select_field, message.chat.id
#     )
#     bot.send_message(
#         message.chat.id,
#         texts.SELECT_FIELD,
#         reply_markup=keyboards.get_reply_keyboard(texts.FIELD_LIST, ["/cancel"]),
#     )
#
#
# @logged_execution
# def handle_cancel_change_data(message, bot, pool):
#     bot.delete_state(message.from_user.id, message.chat.id)
#     bot.send_message(
#         message.chat.id,
#         texts.CANCEL_CHANGE,
#         reply_markup=keyboards.EMPTY,
#     )
#
#
# @logged_execution
# def handle_choose_field_to_change(message, bot, pool):
#     if message.text not in texts.FIELD_LIST:
#         bot.send_message(
#             message.chat.id,
#             texts.UNKNOWN_FIELD,
#             reply_markup=keyboards.get_reply_keyboard(texts.FIELD_LIST, ["/cancel"]),
#         )
#         return
#
#     bot.set_state(
#         message.from_user.id, states.ChangeDataState.write_new_value, message.chat.id
#     )
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data["field"] = message.text
#
#     bot.send_message(
#         message.chat.id,
#         texts.WRITE_NEW_VALUE.format(message.text),
#         reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
#     )
#
#
# @logged_execution
# def handle_save_changed_data(message, bot, pool):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         field = data["field"]
#
#     new_value = message.text
#
#     if field == "age" and not new_value.isdigit():
#         bot.send_message(
#             message.chat.id,
#             texts.AGE_IS_NOT_NUMBER,
#             reply_markup=keyboards.get_reply_keyboard(["/cancel"]),
#         )
#         return
#     elif field == "age":
#         new_value = int(new_value)
#
#     bot.delete_state(message.from_user.id, message.chat.id)
#     current_data = db_model.get_user_info(pool, message.from_user.id)
#     current_data[field] = new_value
#     db_model.update_user_data(pool, **current_data)
#
#     bot.send_message(
#         message.chat.id,
#         texts.CHANGE_DATA_DONE,
#         reply_markup=keyboards.EMPTY,
#     )
