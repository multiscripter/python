import threading
import unittest

from rabbitmq.ch01_hello_world.BlockingReceiver import BlockingReceiver
from rabbitmq.ch01_hello_world.BlockingSender import BlockingSender

# pytest -p no:cacheprovider ./


class TestCh01(unittest.TestCase):
    """Test suites for chapter 01."""

    def test_ch01(self):
        queue_name = 'ch01_queue'
        msg = 'Hello, world!'
        receiver = BlockingReceiver()
        s = BlockingSender()

        def start_receiver(r):
            r.connect(queue=queue_name)
            print('receiver.connected()')
            r.receive()
            print('receiver.receiving()')

        #def start_sender(s):

        tr = threading.Thread(target=start_receiver, args=(receiver,))
        #ts = threading.Thread(target=start_sender, args=(sender,))
        tr.start()
        #ts.start()
        tr.join()
        #ts.join()

        s.connect(queue=queue_name)
        s.send(msg)
        s.close()

        receiver.close()
        print('receiver closed.')
        self.assertEqual(msg, receiver.msg)
