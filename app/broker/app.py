from faststream import FastStream
from faststream.kafka import KafkaBroker
from aiogram.types import InputMediaPhoto
from app.broker.messages import Inference
from aiogram.types import URLInputFile
from app.config import bot

from app.config import settings


broker = KafkaBroker(settings.KAFKA_URL)


app = FastStream(broker)

broker_send = broker.publisher("photo")

@broker.subscriber("photo_out")
async def handler(msg: Inference):
    media = []
    for photo in msg.src_marked:
        image = URLInputFile(
        settings.s3_url +'/'+photo, filename="python-logo.png"
        )
        media.append(InputMediaPhoto(media=image))
    await bot.send_media_group(chat_id=msg.user,
                            media=media)