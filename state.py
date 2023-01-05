from aiogram.dispatcher.filters.state import State, StatesGroup


class ClientStateGroup(StatesGroup):
    name = State()
    surname = State()
    phone = State()
    email = State()