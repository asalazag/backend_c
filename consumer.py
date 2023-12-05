import os
import json

import pika
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'BackendProject.settings'
django.setup()

from BackendApp.views import create_warehouses


params = pika.URLParameters('amqp://ekpnwbki:zuLt7wJ0rDS_0mMDGtJpPT1BELS3Ixr5@moose.rmq.cloudamqp.com/ekpnwbki')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='backend')

def callback(ch, method, properties, body):
    data = json.loads(body)

    response = None
    message = None
    if properties.content_type == 'create_warehouse':
        response, message = create_warehouses(data)

    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         properties.correlation_id),
                     body='{{"response":"{}", "message":"{}"}}'.format(str(response),message))

channel.basic_consume(queue='backend', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

channel.close()