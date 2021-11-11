from aiogram.types import ReplyKeyboardMarkup


def start_language_buttons():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(*LANGUAGES.values())
    return markup
