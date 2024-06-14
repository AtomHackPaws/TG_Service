from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from app.keyboards.start import get_start_inline_buttons
from app.callbacks_factory.base import UserCallbackData
from magic_filter import F

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    # TODO create_user
    builder = get_start_inline_buttons()
    await message.answer("Выберите действие:", reply_markup=builder)


@start_router.callback_query(UserCallbackData.filter(F.action == "get_user_id"))
async def send_random_value(
    callback: CallbackQuery,
):
    await callback.message.answer(f"Ваш id: {callback.from_user.id}")
