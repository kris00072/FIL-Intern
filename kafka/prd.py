from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging as log
producer=KafkaProducer(bootstrafp_servers=['localhost:9092'])
future=producer.send('zomato',b'krishan')

try:
    record_metadata=future.get(timeout=10)
except KafkaError:
    log.exception()
    pass

print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)
