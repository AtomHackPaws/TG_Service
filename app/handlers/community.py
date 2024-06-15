from aiogram import Router
from aiogram import types
from app.config import settings, bot
from magic_filter import F
from aiogram.methods import SendMediaGroup
from app.types import Album
from aiogram.types import CallbackQuery, InputMediaPhoto
from app.keyboards.community import get_community_buttons
from app.callbacks_factory.base import CommunityCallbackData
from app.states.community import Community
from aiogram.fsm.context import FSMContext

comunity_router = Router()


@comunity_router.callback_query(
    CommunityCallbackData.filter(F.action == "help_community")
)
async def community_ask_anonymous(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Выберите, как хотите отправить сообщение в сообщество, анонимно?",
        reply_markup=get_community_buttons(),
    )


@comunity_router.callback_query(
    CommunityCallbackData.filter(F.action.startswith("anonymous_"))
)
async def answer_community_send(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Отправьте сообщение которое хотите опубликовать в комьюнити:",
        reply_markup=None,
    )
    await state.set_state(Community.send)
    await state.update_data(send=True if "yes" in callback.data else False)


async def add_not_anonymous(data_state: dict, message_text: str | None, user_name):
    if message_text:
        if not data_state["send"]:
            message_text += f"\n Отправил сообщение: @{user_name}"
    else:
        if not data_state["send"]:
            message_text = f"\n Отправил сообщение: @{user_name}"
    return message_text


@comunity_router.message(F.media_group_id, Community.send)
async def send_media_group(message: types.Message, album: Album, state: FSMContext):
    data = await state.get_data()
    caption = await add_not_anonymous(data, album.caption, message.from_user.username)
    new_message: SendMediaGroup = album.copy_to(chat_id=settings.CHANNEL_ID)
    new_message.media[0].caption = caption
    await bot.send_media_group(**dict(new_message))


@comunity_router.message(F.photo, Community.send)
async def send_photo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    media = []
    caption = await add_not_anonymous(data, message.caption, message.from_user.username)
    media.append(InputMediaPhoto(media=message.photo[-1].file_id, caption=caption))
    await bot.send_media_group(settings.CHANNEL_ID, media)


@comunity_router.message(F.video, Community.send)
async def send_video(message: types.Message, state: FSMContext):
    data = await state.get_data()
    caption = await add_not_anonymous(data, message.caption, message.from_user.username)
    media = InputMediaPhoto(media=message.video.file_id, caption=caption)
    await bot.send_media_group(settings.CHANNEL_ID, media)


@comunity_router.message(F.text, Community.send)
async def send_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    caption = await add_not_anonymous(data, message.caption, message.from_user.username)
    message.caption = caption
    await bot.send_media_group(settings.CHANNEL_ID, message)
