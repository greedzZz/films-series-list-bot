START = ("Бот успешно запущен!\n\n"
         "Список команд:\n"
         "/show\n"
         "/add\n"
         "/update\n"
         "/delete\n")
NOT_STARTED = "Прежде чем использовать бота вперые, введите /start"
EXISTS = "Фильм/сериал с таким названием уже есть в вашем списке."
NOT_EXISTS = "Фильма/сериала с таким названием нет в вашем списке."

ADD = ("Введите название фильма/сериала для добавления в список "
       "(название не должно совпадать с другими фильмами/сериалами в вашем списке):")
ADD_CANCEL = "Добавление фильма/сериала было отменено."
ADD_SUCCESS = "Фильм/сериал \"{}\" успешно добавлен."

DELETE = "Введите название фильма/сериала для удаления из списка:"
DELETE_CANCEL = "Удаление фильма/сериала было отменено."
DELETE_SUCCESS = "Фильм/сериал \"{}\" успешно удалён."

UPDATE = "Введите название фильма/сериала из списка для редактирования:"
UPDATE_CHOOSE = "Выберите, что вы хотите отредактировать у фильма/сериала \"{}\":"
UPDATE_UNKNOWN = "Редактировать можно только следующие параметры:\n{}\n{}\n{}\n{}"
UPDATE_ENTER = "Введите новое значение параметра \"{}\":"
UPDATE_WRONG_TYPE = "Тип должен быть только одним из следующих значений:\n{}\n{}"
UPDATE_WRONG_YEAR = "Год должен быть целым положительным числом."
UPDATE_LIST = ["type", "year", "country", "note"]
UPDATE_TYPE_LIST = ["film", "serial"]
UPDATE_CANCEL = "Редактирование фильма/сериала было отменено."
UPDATE_SUCCESS = "Фильм/сериал \"{}\" успешно отредактирован."


# START = (
#     "Hello! This is a simple bot that can store your name and age, "
#     "show them back to you and delete them if requested.\n\n"
#     "List of commands:\n"
#     "/start\n"
#     "/register\n"
#     "/show_data\n"
#     "/delete_account"
# )
#
# FIRST_NAME = "Enter your first name."
# LAST_NAME = "Enter your last name."
# AGE = "Enter your age."
# AGE_IS_NOT_NUMBER = "Age should be a positive number, try again."
#
# SHOW_DATA = "First name: {}\nLast name: {}\nAge: {}"
#
# DATA_IS_SAVED = "Your data is saved!\n" + SHOW_DATA
# ALREADY_REGISTERED = "You are already registered!\n" + SHOW_DATA
# SHOW_DATA_WITH_PREFIX = "Your data:\n" + SHOW_DATA
#
# NOT_REGISTERED = "You are not registered yet, try /register."
#
# CANCEL_REGISTER = "Cancelled! Your data is not saved."
#
# DELETE_ACCOUNT = "Are you sure you want to delete your account?"
# DELETE_ACCOUNT_OPTIONS = {"Yes!": True, "No..": False}
# DELETE_ACCOUNT_UNKNOWN = "I don't understand this command."
# DELETE_ACCOUNT_DONE = "Done! You can /register again."
# DELETE_ACCOUNT_CANCEL = "Ok, stay for longer!"
#
# FIELD_LIST = ["first_name", "last_name", "age"]
# UNKNOWN_FIELD = "Unknown field, choose a field from the list below:"
# SELECT_FIELD = "Choose a field to change:"
# WRITE_NEW_VALUE = "Write new value for the field {}"
# CANCEL_CHANGE = "Cancelled! Your data is not changed."
# CHANGE_DATA_DONE = "Done! Your data is updated."
