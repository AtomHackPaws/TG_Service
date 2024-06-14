from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.callbacks_factory.base import UserCallbackData, CommunityCallbackData


# TODO change buttons
def get_community_buttons() -> InlineKeyboardButton:
    builder = InlineKeyboardBuilder()
    builder.button(text="Да", callback_data=UserCallbackData(action="user_profile"))
    builder.button(text="Нет", callback_data=CommunityCallbackData(action="load_photo"))
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)
