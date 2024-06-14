from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.callbacks_factory.base import (
    UserCallbackData,
    CommunityCallbackData,
    ModelCallbackData,
)


# TODO change buttons
def get_start_inline_buttons() -> InlineKeyboardButton:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Профиль", callback_data=UserCallbackData(action="user_profile")
    )
    builder.button(
        text="Загрузить фотку", callback_data=CommunityCallbackData(action="load_photo")
    )
    builder.button(
        text="Помощь", callback_data=ModelCallbackData(action="help_community")
    )
    builder.button(
        text="Получить свой id", callback_data=UserCallbackData(action="get_user_id")
    )
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)
