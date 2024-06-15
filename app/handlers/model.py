import asyncio
from aiogram import Router
from magic_filter import F
from aiogram.types import CallbackQuery, Message
from app.callbacks_factory.base import CommunityCallbackData
from app.broker import broker_send, Data, PhotoTopic
from app.config import settings, bot
from aiogram.methods import SendMediaGroup
from app.types import Album
from aiogram.types import CallbackQuery
from app.callbacks_factory.base import CommunityCallbackData
from app.s3.s3_client import S3Service

model_router = Router()


async def download_and_upload_media(media, file_type):
    file_info = await bot.get_file(media.file_id)
    filename = f"{media.file_id}.{file_type}"
    downloaded_file = await bot.download_file(file_info.file_path)
    uploaded_link = await S3Service.put_object(filename, downloaded_file)
    return uploaded_link


@model_router.callback_query(CommunityCallbackData.filter(F.action == "load_photo"))
async def load_photo(callback: CallbackQuery):
    # TODO s3 load video/ photo
    await broker_send.publish(
        Data(photo=PhotoTopic(photo=list("dsadsa"), user="dsasda"))
    )
    await callback.message.answer("Отправлено на оценку")


@model_router.message(F.video)
async def send_video(message: Message):
    try:
        if message.video:
            await S3Service.get_s3_client()
            link = await download_and_upload_media(message.video, "mp4")
            await message.answer(link)
    finally:
        await S3Service.close_s3_session()


@model_router.message(F.photo)
async def send_photo(message: Message):
    try:
        if message.photo:
            await S3Service.get_s3_client()
            link = await download_and_upload_media(message.photo[-1], "jpg")
            await message.answer(link)
    finally:
        await S3Service.close_s3_session()


@model_router.message(F.media_group_id)
async def send_post_to_channel(message: Message, album: Album):
    message: SendMediaGroup = album.copy_to(chat_id=settings.CHANNEL_ID)
    # TODO анонимно или нет message.from_user.username
    # await bot.send_media_group(**dict(messag))

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
        await message.reply("Сообщение отправлено в комьюнити!")
        await message.answer("\n".join(links))
    finally:
        await S3Service.close_s3_session()
