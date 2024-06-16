import asyncio
import json
from aiogram import Router
from magic_filter import F
from aiogram.types import CallbackQuery, Message
from app.callbacks_factory.base import ModelCallbackData
from app.broker import broker_send, Data, PhotoTopic
from app.config import settings, bot
from aiogram.methods import SendMediaGroup
from app.db.connection import Transaction
from app.types import Album
from app.s3.s3_client import S3Service
from aiogram.fsm.context import FSMContext
from app.states.model import Model

from app.models import Result


model_router = Router()


async def download_and_upload_media(media, file_type):
    file_info = await bot.get_file(media.file_id)
    filename = f"{media.file_id}.{file_type}"
    downloaded_file = await bot.download_file(file_info.file_path)
    uploaded_link = await S3Service.put_object(filename, downloaded_file)
    return uploaded_link


@model_router.callback_query(ModelCallbackData.filter(F.action == "load_photo"))
async def load_photo(callback: CallbackQuery, state: FSMContext):
    # TODO s3 load video/ photo

    await callback.message.edit_text(
        text="Отправьте сообщение которое хотите опубликовать в комьюнити:",
        reply_markup=None,
    )
    await state.set_state(Model.send)


@model_router.message(F.video, Model.send)
async def send_video(message: Message):
    try:
        if message.video:
            await S3Service.get_s3_client()
            link = await download_and_upload_media(message.video, "mp4")

            await broker_send.publish(
                Data(photo=PhotoTopic(photo=[link], user=message.from_user.id))
            )

            async with Transaction():
                await Result.create_result(
                    result=json.dumps([{"score": 0.0, "label": 0, "link": ""}]),
                    profile_id=message.from_user.id,
                )

            await message.answer(link)
    finally:
        await S3Service.close_s3_session()


@model_router.message(F.photo, Model.send)
async def send_photo(message: Message):
    try:
        if message.photo:
            await S3Service.get_s3_client()
            link = await download_and_upload_media(message.photo[-1], "jpg")

            await broker_send.publish(
                Data(photo=PhotoTopic(photo=[link], user=message.from_user.id))
            )

            async with Transaction():
                await Result.create_result(
                    result=json.dumps([{"score": 0.0, "label": 0, "link": ""}]),
                    profile_id=message.from_user.id,
                )

            await message.answer(link)
    finally:
        await S3Service.close_s3_session()


@model_router.message(F.media_group_id, Model.send)
async def send_post_to_channel(message: Message, album: Album):
    message: SendMediaGroup = album.copy_to(chat_id=settings.CHANNEL_ID)
    try:
        await S3Service.get_s3_client()

        tasks = []
        if album.photo:
            tasks.extend(
                [download_and_upload_media(media, "jpg") for media in album.photo]
            )
        if album.video:
            tasks.extend(
                [download_and_upload_media(media, "mp4") for media in album.video]
            )
        links = await asyncio.gather(*tasks)

        await broker_send.publish(
            Data(photo=PhotoTopic(photo=links, user=message.from_user.id))
        )

        async with Transaction():
            await Result.create_result(
                result=json.dumps([{"score": 0.0, "label": 0, "link": ""}]),
                profile_id=message.from_user.id,
            )

        await message.reply("Сообщение отправлено в комьюнити!")
        await message.answer("\n".join(links))
    finally:
        await S3Service.close_s3_session()
