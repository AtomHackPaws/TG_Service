from aiogram import Router
from aiogram.types import CallbackQuery
from app.callbacks_factory.base import UserCallbackData
from magic_filter import F

profile_router = Router()


@profile_router.callback_query(UserCallbackData.filter(F.action == "user_profile"))
async def send_random_value(
    callback: CallbackQuery,
):
    await callback.message.answer(f"Ваш id: {callback.from_user.id}")
