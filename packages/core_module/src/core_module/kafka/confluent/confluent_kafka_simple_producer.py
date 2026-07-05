#!/usr/bin/env python
# =============================================================================
#
# Produce messages to Confluent Cloud
# Using Confluent Python Client for Apache Kafka
#
# =============================================================================
import random
from time import sleep

from core_module.kafka.confluent.confluent_kafka_ConfigFactory import KafkaConfigFactory
from core_module.kafka.confluent.confluent_kafka_ProducerFactory import ProducerFactory
from core_module.kafka.confluent.confluent_kafka_usecase import synchronous_produce

#
#
#


if __name__ == '__main__':

    TOPIC = "simple-text-topic"
    # Create Producer instance
    producer_config = KafkaConfigFactory.producer('PLAINTEXT')
    producer = ProducerFactory.simple(producer_config)
    produced_records = 0

    while True:
        #
        produced_records += 1
        #
        KEYS = ["A", "B", "C", "D"]
        record_key = random.choice(KEYS)
        # record_value = json.dumps({'key': record_key, 'index': produced_records})
        record_value = "This is test event {} of type {}".format(produced_records, record_key)
        event = {"key": record_key, "value": record_value}
        #
        synchronous_produce(producer,TOPIC,event)
        sleep(1)

    print("{} messages were produced to topic {}!".format(delivered_records, topic))

