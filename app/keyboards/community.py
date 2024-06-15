from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.callbacks_factory.base import UserCallbackData, CommunityCallbackData


def get_community_buttons() -> InlineKeyboardButton:
    inline_kb_full = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Да",
                    callback_data=CommunityCallbackData(action="anonymous_yes").pack(),
                ),
                InlineKeyboardButton(
                    text="Нет",
                    callback_data=CommunityCallbackData(action="anonymous_no").pack(),
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
