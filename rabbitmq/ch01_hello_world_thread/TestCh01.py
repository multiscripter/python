import unittest
from threading import Timer

from rabbitmq.ch01_hello_world.BlockingSender import BlockingSender
from rabbitmq.ch01_hello_world_thread.BlockingReceiver import BlockingReceiver

# pytest -p no:cacheprovider ./ch01_hello_world_thread/*


class TestCh01(unittest.TestCase):
    """Test suites for ch01_hello_world_thread."""

    def test_ch01(self):
        queue = 'ch01thread'
        messages = [
            'test-message-1',
            'shutdown receiver'
        ]

        sender = BlockingSender()
        sender.connect(queue=queue)
        for message in messages:
            sender.send(message)
        sender.close()

        receiver = BlockingReceiver()
        receiver.start()
        receiver.connect(queue=queue)

        t = Timer(1.0, receiver.close)
        t.start()
        # Не ждать окончания работы BlockingReceiver.
        # receiver.join()
        receiver.receive()

        self.assertEqual(messages[0], receiver.messages[0])
        print(receiver.messages, flush=True)
