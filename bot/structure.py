from functools import partial

from telebot import TeleBot, custom_filters

from bot import handlers as handlers
from bot import states as bot_states


class Handler:
    def __init__(self, callback, **kwargs):
        self.callback = callback
        self.kwargs = kwargs


def get_start_handlers():
    return [
        Handler(callback=handlers.handle_start, commands=["start"])
    ]


def get_add_handlers():
    return [
        Handler(callback=handlers.handle_add, commands=["add"]),
        Handler(callback=handlers.handle_cancel_add, commands=["cancel"], state=bot_states.AddState.name),
        Handler(callback=handlers.handle_add_name, state=bot_states.AddState.name)
    ]


def get_delete_handlers():
    return [
        Handler(callback=handlers.handle_delete, commands=["delete"]),
        Handler(callback=handlers.handle_cancel_delete, commands=["cancel"], state=bot_states.DeleteState.name),
        Handler(callback=handlers.handle_delete_name, state=bot_states.DeleteState.name)
    ]


def get_update_handlers():
    return [
        Handler(callback=handlers.handle_update, commands=["update"]),
        Handler(
            callback=handlers.handle_cancel_update,
            commands=["cancel"],
            state=[
                bot_states.UpdateState.name,
                bot_states.UpdateState.select_field,
                bot_states.UpdateState.write_new_value
            ],
        ),
        Handler(callback=handlers.handle_update_name, state=bot_states.UpdateState.name),
        Handler(callback=handlers.handle_update_choose_field, state=bot_states.UpdateState.select_field),
        Handler(callback=handlers.handle_update_enter_value, state=bot_states.UpdateState.write_new_value)
    ]


def get_show_handlers():
    return [
        Handler(callback=handlers.handle_show, commands=["show"]),
        Handler(
            callback=handlers.handle_cancel_show,
            commands=["cancel"],
            state=[
                bot_states.ShowState.sort,
                bot_states.ShowState.select_sort_field,
                bot_states.ShowState.filter,
                bot_states.ShowState.select_filter_field,
                bot_states.ShowState.write_filter_value
            ],
        ),
        Handler(callback=handlers.handle_show_sort, state=bot_states.ShowState.sort),
        Handler(callback=handlers.handle_show_sort_choose_field, state=bot_states.ShowState.select_sort_field),
        Handler(callback=handlers.handle_show_filter, state=bot_states.ShowState.select_filter_field),
        Handler(callback=handlers.handle_show_filter_choose_field, state=bot_states.ShowState.select_filter_field),
        Handler(callback=handlers.handle_show_filter_enter_value, state=bot_states.ShowState.write_filter_value)
    ]


def create_bot(bot_token, pool):
    state_storage = bot_states.StateYDBStorage(pool)
    bot = TeleBot(bot_token, state_storage=state_storage)

    handlers = []
    handlers.extend(get_start_handlers())
    handlers.extend(get_add_handlers())
    handlers.extend(get_delete_handlers())
    handlers.extend(get_update_handlers())
    handlers.extend(get_show_handlers())

    for handler in handlers:
        bot.register_message_handler(
            partial(handler.callback, pool=pool), **handler.kwargs, pass_bot=True
        )

    bot.add_custom_filter(custom_filters.StateFilter(bot))
    return bot
