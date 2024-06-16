from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from app.keyboards.start import get_start_inline_buttons
from app.callbacks_factory.base import UserCallbackData
from magic_filter import F

from app.models import Profile
from app.db import Transaction

start_router = Router()


@start_router.callback_query(UserCallbackData.filter(F.action == "start"))
@start_router.message(Command("start"))
async def cmd_start(message: Message):
    builder = get_start_inline_buttons()
    user_data = message.from_user
    if type(message) == CallbackQuery:
        await message.message.delete()
        await message.message.answer("Выберите действие:", reply_markup=builder)
    async with Transaction():
        await Profile.create_user(id=user_data.id, username=user_data.username)
    message = await message.answer("Выберите действие:", reply_markup=builder)


@start_router.callback_query(UserCallbackData.filter(F.action == "get_user_id"))
async def send_user_id(
    callback: CallbackQuery,
):
    await callback.message.answer(f"Ваш id: {callback.from_user.id}")
