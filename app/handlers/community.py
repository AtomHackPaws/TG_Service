import asyncio
from typing import Any
from aiogram import Router
from aiogram import types
from app.config import settings, bot
from magic_filter import F
from aiogram.methods import SendMediaGroup
from app.types import Album

from app.s3.s3_client import S3Service

comunity_router = Router()


# @comunity_router.callback_query(CommunityCallbackData.filter(F.action == "help_community"))
# async def cmd_food(message: types.Message,
#                    state: FSMContext):
#     await message.answer(
#         text="Выберите как хотите отправить сообщение",
#         reply_markup=make_row_keyboard(available_food_names)
#     )
#     await state.set_state(Community.anonymous)


async def download_and_upload_media(media, file_type):
    file_info = await bot.get_file(media.file_id)
    filename = f"{media.file_id}.{file_type}"
    downloaded_file = await bot.download_file(file_info.file_path)
    uploaded_link = await S3Service.put_object(filename, downloaded_file)
    return uploaded_link
    
    
@comunity_router.message(F.media_group_id)
async def send_post_to_channel(message: types.Message, album: Album):
    messag: SendMediaGroup = album.copy_to(chat_id=settings.CHANNEL_ID)
    # TODO анонимно или нет message.from_user.username
    # await bot.send_media_group(**dict(messag))
    
    await S3Service.get_s3_client()
    
    tasks = []
    if album.photo:
        tasks.extend([download_and_upload_media(media, 'jpg') for media in album.photo])
    if album.video:
        tasks.extend([download_and_upload_media(media, 'mp4') for media in album.video])
    links = await asyncio.gather(*tasks)
    await message.reply("Сообщение отправлено в комьюнити!")
    await message.answer('\n'.join(links))


@comunity_router.message(F.photo)
async def send_photo(message: types.Message):
    if message.photo:
        await S3Service.get_s3_client()
        link = await download_and_upload_media(message.photo[-1], 'jpg')
        await message.answer(link)


@comunity_router.message(F.video)
async def send_video(message: types.Message):
    if message.video:
        await S3Service.get_s3_client()
        link = await download_and_upload_media(message.video, 'mp4')
        await message.answer(link)
