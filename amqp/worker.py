#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("[x] Received %s" % body)
    time.sleep(2)
    print("Done")


channel.basic_consume(callback, queue='hello', no_ack=True)

print "Waiting for messages. To exit press CTRL+C"
channel.start_consuming()
