from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationState(StatesGroup):
    language = State()
    account = State()
