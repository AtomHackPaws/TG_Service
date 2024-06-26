from aiogram import Dispatcher, F
from app.config import bot
from app.handlers import list_of_routes
from app.middlewares.album import AlbumMiddleware
from app.broker import broker
import logging
from aiogram.types import ChatMemberUpdated
from aiogram.filters.chat_member_updated import \
    ChatMemberUpdatedFilter, MEMBER, KICKED

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


async def on_startup() -> None:
    await broker.start()


async def shutdown() -> None:
    await broker.close()


dp.startup.register(on_startup)
dp.shutdown.register(shutdown)

dp.message.filter(F.chat.type == "private")
dp.message.middleware(AlbumMiddleware())


def bind_routes(dp: Dispatcher) -> None:
    """
    Bind all routes to Dispatcher.
    """
    for route in list_of_routes:
        dp.include_router(route)

async def main():
    bind_routes(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot,
        allowed_updates=["message", "inline_query", "my_chat_member", "callback_query"],
    )
