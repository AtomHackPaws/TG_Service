from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.callbacks_factory.base import (
    UserCallbackData,
    CommunityCallbackData,
    ModelCallbackData,
)


def get_start_inline_buttons() -> InlineKeyboardButton:
    inline_kb_full = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Профиль",
                    callback_data=UserCallbackData(action="user_profile").pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Загрузить фотку",
                    callback_data=ModelCallbackData(action="load_photo").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Помощь",
                    callback_data=CommunityCallbackData(action="help_community").pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Получить свой id",
                    callback_data=UserCallbackData(action="get_user_id").pack(),
                ),
            ],
        ],
    )
    return inline_kb_full
