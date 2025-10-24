"""Consumer"""

from kafka import KafkaConsumer

TOPIC = 'PRODUCTS'

# Config:
# - auto_offset_reset='earliest': start reading message from topic begin.
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='group1'
)

print("\n")
print("|========================================|")
print("|    🚀 [CONSUMER MODULE - ACTIVE] 🚀    |")
print(f"|        Listening Topic: {TOPIC}       |")
print("|========================================|")
print("|         Waiting for messages...        |")
print("|             (Ctrl+C to end)            |")
print("|========================================|")
print("\n")

print("|========================================|")
print("|            📩 [MESSAGES] 📩            |")
print("|========================================|")
print("\n")

try:
    for message in consumer:
        # message.value is a byte object, decodifying to string
        content = message.value.decode('utf-8')
        print(f"[Received: {content} | Partition: {message.partition} | Offset: {message.offset} ]")

except KeyboardInterrupt:
    print("\n[CONSUMER ENDED]")
finally:
    consumer.close()
    