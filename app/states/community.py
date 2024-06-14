from aiogram.fsm.state import State, StatesGroup


class Community(StatesGroup):
    anonymous = State()
    dsa = State()
