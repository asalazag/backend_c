import json
import pika
import uuid


# def publish(method, body, routing_key):
#     properties = pika.BasicProperties(method)
#     params = pika.URLParameters('amqps://ldpwyhya:1dxsye-raZwwQK0p9L_Jrj0DuRFjcMR0@shark.rmq.cloudamqp.com/ldpwyhya')
#     connection = pika.BlockingConnection(params)
#     channel = connection.channel()
#     channel.basic_publish(exchange='', routing_key=routing_key, body=json.dumps(body), properties=properties)
#     channel.close()

class PublishAMQP(object):

    def __init__(self):
        self.params = pika.URLParameters('amqp://ekpnwbki:zuLt7wJ0rDS_0mMDGtJpPT1BELS3Ixr5@moose.rmq.cloudamqp.com/ekpnwbki')
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(queue=self.callback_queue, on_message_callback=self.on_response, auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def publish(self, method, body, routing_key):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.properties = pika.BasicProperties(
                content_type=method,
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            )
        self.channel.basic_publish(exchange='',routing_key=routing_key,properties=self.properties,body=json.dumps(body))
        while self.response is None:
            self.connection.process_data_events()
        return self.response


