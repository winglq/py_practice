#!/usr/bin/env python
import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
message = ' '.join(sys.argv[1:]) or 'Hello World'
channel.basic_publish(exchange='', routing_key='hello', body=message,
                      properties=pika.BasicProperties(delivery_mode=2))
print "Send %s" % message
connection.close()
