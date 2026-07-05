#!/usr/bin/env python
#
# confluent_kafka_SerializingProducer.py -b kafkabroker.sandbox.net:9092 -s http://schemaregistry.sandbox.net:8081 -t user-avro-topic
#
#
# This is a simple example of the SerializingProducer using Avro.
#
from core_module.models.User import User
from datetime import datetime
from time import sleep

from core_module.kafka.confluent.confluent_kafka_ConfigFactory import KafkaConfigFactory
from core_module.kafka.confluent.confluent_kafka_ProducerFactory import ProducerFactory


#
#
#
def serializer_sink(args):

    topic = args['topic']
    producer_conf = KafkaConfigFactory.producer(args['auth_type'])
    producer = ProducerFactory.serializer(producer_conf,"conf/avro/user-record.avsc", User.to_dict)

    #
    print("Producing user records to topic {}. ^C to exit.".format(topic))
    while True:
        # Serve on_delivery callbacks from previous calls to produce()
        producer.poll(0.0)
        try:
            #
            # int(time.timestamp() * 1000)
            event_datetime = datetime.now().timestamp()
            # d_in_ms = int(event_datetime.strftime("%S"))
            user = User.random()
            key = user.uuid
            producer.produce(topic=topic, key=key, value=user)
            sleep(1)
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Invalid input, discarding record...")
            continue

    print("\nFlushing records...")
    producer.flush()


if __name__ != '__main__':
    pass
else:
    args = {
        'topic': "user-avro-topic",
        'auth_type': "PLAINTEXT"
    }
    serializer_sink(args)

#