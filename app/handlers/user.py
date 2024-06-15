from aiogram import Router
from aiogram.types import CallbackQuery
from app.callbacks_factory.base import UserCallbackData
from app.keyboards.user import get_user_inline_buttons
from magic_filter import F

profile_router = Router()


@profile_router.callback_query(UserCallbackData.filter(F.action == "user_profile"))
async def send_user_profile(
    callback: CallbackQuery,
):
    await callback.message.edit_text(
        text="Выберите действие", reply_markup=get_user_inline_buttons()
    )


@profile_router.callback_query(UserCallbackData.filter(F.action == "add_master"))
async def add_master(
    callback: CallbackQuery,
):
    await callback.message.edit_text(text="Введите id Мастера:", reply_markup=None)
    # TODO set state


@profile_router.callback_query(UserCallbackData.filter(F.action == "send_master"))
async def send_master(
    callback: CallbackQuery,
):
    await callback.message.edit_text(
        text="Прикрепите фото, и мы отправим мастеру.",
        reply_markup=get_user_inline_buttons(),
    )
