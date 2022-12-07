import os

from kafka import KafkaConsumer
from helper import save_location

TOPIC_NAME = os.environ.get("TOPIC_NAME", "locations")
KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "192.168.178.31:9092")

# Create the kafka consumer
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

while True:
    for message in consumer:
        location_data = message.value.decode('utf-8')
        save_location(location_data)
