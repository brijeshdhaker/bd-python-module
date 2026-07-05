from core_module.kafka.confluent.confluent_kafka_ConfigFactory import KafkaConfigFactory
from core_module.kafka.confluent.confluent_kafka_ConsumerFactory import ConsumerFactory
from core_module.kafka.confluent.confluent_kafka_usecase import at_most_once_consume
#
#
#
TOPIC = "simple-text-topic"
consumer_config = KafkaConfigFactory.consumer('SASL_SSL')

#
#     'enable.auto.commit': False,
#
consumer = ConsumerFactory.simple(consumer_config)
consumer.subscribe([TOPIC])
MIN_COMMIT_COUNT = 10
try:

    at_most_once_consume(consumer, TOPIC)

except:

    print("Something went wrong")

finally:
    # Close down consumer to commit final offsets.
    consumer.close()
