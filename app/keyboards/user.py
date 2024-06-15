from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.callbacks_factory.base import (
    UserCallbackData,
)

def get_user_inline_buttons() -> InlineKeyboardButton:
    inline_kb_full = InlineKeyboardMarkup(row_width=2,inline_keyboard=[
    [
    InlineKeyboardButton(
        text="Отправить Мастеру", callback_data=UserCallbackData(action="send_master").pack()
    ),
    ],
    [InlineKeyboardButton(
        text="Добавить мастера", callback_data=UserCallbackData(action="add_master").pack()
    )],
    [InlineKeyboardButton(
        text="История", callback_data=UserCallbackData(action="history").pack()
    )],
    [InlineKeyboardButton(
        text="Назад", callback_data=UserCallbackData(action="start").pack()
    )]
    ])
    return inline_kb_full