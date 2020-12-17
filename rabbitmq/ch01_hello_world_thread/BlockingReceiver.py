import pika
import threading

from pika.exceptions import StreamLostError


class BlockingReceiver(threading.Thread):
    def __init__(self):
        super().__init__()
        self.ch = None
        self.conn = None
        self.messages = []
        self.queue = None

    def callback(self, ch, method, properties, body):
        body = body.decode('ascii')
        self.messages.append(body)
        print(f'BlockingReceiver message: {body}')
        # Нет нормального механизма отключения канала в BlockingConnection.
        # Варианты решения:
        # 1. https://pika.readthedocs.io/en/latest/examples/blocking_consumer_generator.html
        # 2. SelectConnection
        if body == 'shutdown receiver':
            self.close()

    def close(self):
        try:
            self.ch.stop_consuming()
            if self.ch.is_open:
                self.ch.close()
            if self.conn.is_open:
                self.conn.close()
        except StreamLostError:
            print('BlockingReceiver: closed')

    def connect(self, host: str = 'localhost', queue: str = 'default'):
        self.queue = queue
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(host=host)
        )
        self.ch = self.conn.channel()
        self.ch.queue_declare(self.queue)
        print(f'BlockingReceiver: connected to {self.queue}')

    def receive(self):
        self.ch.basic_consume(
            queue=self.queue,
            on_message_callback=self.callback,
            auto_ack=True
        )
        print(f'BlockingReceiver: waiting for messages')
        self.ch.start_consuming()
