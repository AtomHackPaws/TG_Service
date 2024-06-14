from aiogram import Router
from magic_filter import F
from aiogram.types import CallbackQuery
from app.callbacks_factory.base import CommunityCallbackData


model_router = Router()


@model_router.callback_query(CommunityCallbackData.filter(F.action == "load_photo"))
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer(f"Ваш id: {callback.from_user.id}")
