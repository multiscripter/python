import pika


class BlockingSender:
    def __init__(self):
        self.conn = None
        self.ch = None
        self.queue = None

    def close(self):
        self.conn.close()
        print(f'BlockingSender: closed', flush=True)

    def connect(self, host: str = 'localhost', queue: str = 'default'):
        self.queue = queue
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(host=host)
        )
        self.ch = self.conn.channel()
        self.ch.queue_declare(self.queue)

    def send(self, msg: str, routing_key: str = None):
        if not self.conn:
            self.connect()
        if routing_key is None:
            routing_key = self.queue
        self.ch.basic_publish(
            exchange='', routing_key=routing_key, body=msg
        )
        print(f'BlockingSender message: {msg}', flush=True)


if __name__ == '__main__':
    sender = BlockingSender()
    sender.connect(queue='default_queue')
    sender.send('Hello, world!')
    sender.close()
