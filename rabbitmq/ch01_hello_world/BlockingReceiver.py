import pika


class BlockingReceiver:
    def __init__(self):
        self.conn = None
        self.ch = None
        # self.msg = None
        self.queue = None

    def callback(self, ch, method, properties, body):
        print(f'BlockingReceiver: {body}')
        # self.msg = body

    def close(self):
        self.ch.stop_consuming()
        self.conn.close()

    def connect(self, queue: str, host: str = 'localhost'):
        self.queue = queue
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(host=host)
        )
        self.ch = self.conn.channel()
        self.ch.queue_declare(self.queue)

    def receive(self):
        self.ch.basic_consume(
            queue=self.queue,
            on_message_callback=self.callback,
            auto_ack=True
        )
        print(f'BlockingReceiver: Waiting for messages')
        self.ch.start_consuming()


if __name__ == '__main__':
    try:
        receiver = BlockingReceiver()
        receiver.connect(queue='default_queue')
        receiver.receive()
    except KeyboardInterrupt:
        print('Interrupted')
        exit(0)
