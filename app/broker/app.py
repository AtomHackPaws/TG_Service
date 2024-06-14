from faststream import FastStream, Logger
from faststream.kafka import KafkaBroker

from app.config import settings


broker = KafkaBroker(settings.KAFKA_URL)


app = FastStream(broker)


@broker.subscriber("test_batch")
async def handle_msg(msg, logger: Logger) -> str:
    logger.info(msg)
