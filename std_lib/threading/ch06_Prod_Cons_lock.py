# Проблема "производитель-потребитель" (Producer-Consumer Problem)
# она же "Bounded-buffer problem".

# Решение с использоваием Lock.
# Класс Queue в Python потокобезопасен !!!

import queue
import time
import threading
from concurrent.futures.thread import ThreadPoolExecutor

MSG_LIMIT = 10000


class BoundedBuffer:
    def __init__(self, max_size: int = 10, msg_limit: int = 0):
        self.max_size = max_size
        self.msg_limit = msg_limit
        self.msg_counter = 0
        self.queue = queue.Queue(max_size)
        # При работе с фиксированной очередью/стэком и использовании
        # системы wait/notify, когда потоки висят на мониторе
        # и ждут уведомления, нужно использовать 2 монитора.
        # При использовании одного монитора может произойти deadlock,
        # в случае если при полностью заполненной очереди/стэке
        # блокировку получит поток на запись.
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()

    def get_message(self, name: str) -> str:
        with self.consumer_lock:
            if self.queue.qsize() < 1:
                if self.msg_limit > 0 \
                        and self.msg_limit > self.msg_counter:
                    time.sleep(0.0001)
                else:
                    return ''
            message = self.queue.get()
            print(f'{name} got {message} counter: {self.msg_counter}')
            time.sleep(0.0001)
            return message

    def set_message(self, name: str, message: str) -> None:
        with self.producer_lock:
            if self.msg_limit > 0 and self.msg_limit == self.msg_counter:
                return
            while self.queue.qsize() == self.max_size:
                time.sleep(0.0001)
            self.queue.put(message)
            self.msg_counter += 1
            print(f'{name} put {message} counter: {self.msg_counter}')
            time.sleep(0.0001)


class Producer:
    def __init__(self, name: str, buffer: BoundedBuffer):
        self.buffer = buffer
        self.message = 1
        self.name = name

    def work(self):
        while self.buffer.msg_counter < MSG_LIMIT:
            self.buffer.set_message(self.name, f'{self.name}: {self.message}')
            self.message += 1


class Consumer:
    def __init__(self, name: str, buffer: BoundedBuffer):
        self.buffer = buffer
        self.name = name

    def work(self):
        while self.buffer.msg_counter < MSG_LIMIT:
            self.buffer.get_message(self.name)


def runner(entity):
    entity.work()


buffer = BoundedBuffer(msg_limit=MSG_LIMIT)
with ThreadPoolExecutor(max_workers=100) as executor:
    for a in range(1, 11):
        executor.submit(runner, Producer(f'prod-{a}', buffer))
    for a in range(1, 91):
        executor.submit(runner, Consumer(f'cons-{a}', buffer))
