from aiogram.fsm.state import State, StatesGroup


class QuizState(StatesGroup):
    start = State()
    answer = State()
    menu = State()