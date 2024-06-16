from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.callbacks_factory.base import (
    QuizCallbackData,
    UserCallbackData
)

def get_quiz_buttons() -> InlineKeyboardButton:
    inline_kb_full = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Прилегающие дефекты",
                    callback_data=QuizCallbackData(action="adj").pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Дефекты целостности",
                    callback_data=QuizCallbackData(action="int").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Дефекты геометрии",
                    callback_data=QuizCallbackData(action="geo").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Дефекты постобработки",
                    callback_data=QuizCallbackData(action="pro").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Дефекты невыполнения",
                    callback_data=QuizCallbackData(action="non").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Нет деффектов",
                    callback_data=QuizCallbackData(action="background").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Назад", callback_data=UserCallbackData(action="start").pack()
                )
            ],
        ],
    )
    return inline_kb_full


def get_eazy_quiz_buttons() -> InlineKeyboardButton:
    inline_kb_full = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Да",
                    callback_data=QuizCallbackData(action="adj").pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Нет",
                    callback_data=QuizCallbackData(action="anonymous_no").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Назад", callback_data=UserCallbackData(action="start").pack()
                )
            ],
        ],
    )
    return inline_kb_full


def get_start_quiz_buttons() -> InlineKeyboardButton:
    inline_kb_full = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Да",
                    callback_data=QuizCallbackData(action="start").pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Назад", callback_data=UserCallbackData(action="start").pack()
                )
            ],
        ],
    )
    return inline_kb_full

def get_continue_quiz_buttons() -> InlineKeyboardButton:
    inline_kb_full = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Дальше",
                    callback_data=QuizCallbackData(action="start").pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Назад", callback_data=UserCallbackData(action="start").pack()
                )
            ],
        ],
    )
    return inline_kb_full