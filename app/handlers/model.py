from aiogram import Router
from magic_filter import F
from aiogram.types import CallbackQuery
from app.callbacks_factory.base import CommunityCallbackData
from app.broker import broker_send, Data, PhotoTopic

model_router = Router()


@model_router.callback_query(CommunityCallbackData.filter(F.action == "load_photo"))
async def load_photo(callback: CallbackQuery):
    # TODO s3 load video/ photo
    await broker_send.publish(
        Data(photo=PhotoTopic(photo=list("dsadsa"), user="dsasda"))
    )
    await callback.message.answer("Отправлено на оценку")
