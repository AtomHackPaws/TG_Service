from aiogram import Router
from aiogram import types
from app.config import settings, bot
from magic_filter import F
from aiogram.methods import SendMediaGroup
from app.types import Album


comunity_router = Router()


# @comunity_router.callback_query(CommunityCallbackData.filter(F.action == "help_community"))
# async def cmd_food(message: types.Message,
#                    state: FSMContext):
#     await message.answer(
#         text="Выберите как хотите отправить сообщение",
#         reply_markup=make_row_keyboard(available_food_names)
#     )
#     await state.set_state(Community.anonymous)


@comunity_router.message(F.media_group_id)
async def send_post_to_channel(message: types.Message, album: Album):
    messag: SendMediaGroup = album.copy_to(chat_id=settings.CHANNEL_ID)
    # TODO анонимно или нет message.from_user.username
    await bot.send_media_group(**dict(messag))
    await message.reply("Сообщение отправлено в комьюнити!")
