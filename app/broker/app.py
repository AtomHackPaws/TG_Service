from faststream import FastStream
from faststream.kafka import KafkaBroker

from app.config import settings


broker = KafkaBroker(settings.KAFKA_URL)


app = FastStream(broker)

broker_send = broker.publisher("photo")
