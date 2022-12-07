import json
import logging
import os
import psycopg2

from schemas import LocationSchema
from typing import Dict
from kafka import KafkaProducer

TOPIC_NAME = os.environ.get("TOPIC_NAME", "locations")
KAFKA_SERVER = os.environ.get("KAFKA_SERVER")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-service")

# Create the kafka producer
producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])


def publish_location(location_data):
    print(f"Data to be sent to kafka: {location_data}")
    try:
        encoded_data = json.dumps(location_data).encode('utf-8')
        print(f"Data to be sent to kafka: {encoded_data}")
        producer.send(TOPIC_NAME, encoded_data)
        producer.flush()

        logger.info(f"Published location data {location_data} to kafka successfully.")
    except Exception as ex:
        raise Exception(ex)
