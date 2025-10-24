"""Producer"""

import time
from kafka import KafkaProducer

# Config:
# bootstrap_servers: conect to kafka broker
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: v.encode('utf-8')
)

TOPIC = 'PRODUCTS'

print("\n")
print("|========================================|")
print("|    🚀 [PRODUCER MODULE - ACTIVE] 🚀    |")
print(f"|            Destiny: {TOPIC}           |")
print("|========================================|")
print("|           Sending messages...          |")
print("|             (Ctrl+C to end)            |")
print("|========================================|")
print("\n")

print("|========================================|")
print("|          📨 [SENT MESSAGES] 📨         |")
print("|========================================|")
print("\n")

COUNTER = 0

while True:
    MSG = f'{COUNTER} | Testing...'

    # Envia a mensagem
    producer.send(TOPIC, value=MSG)

    print(f"[Message Sent: {MSG}]")
    COUNTER += 1
    time.sleep(1)

# Garantee that all messages was sent to broker
producer.flush()
print("\n[PRODUCER ENDED]")
