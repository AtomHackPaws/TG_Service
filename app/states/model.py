from aiogram.fsm.state import State, StatesGroup


class Model(StatesGroup):
    send = State()
