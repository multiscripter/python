import threading
from queue import Queue
from threading import Event
import time
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Any

# Использованием класса threading.Event для изменения работы в потоках.

event = Event()


class BoundedBuffer:
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self.queue = Queue(maxsize)
        # При работе с фиксированной очередью/стэком и использовании
        # системы wait/notify, когда потоки висят на мониторе
        # и ждут уведомления, нужно использовать 2 монитора.
        # При использовании одного монитора может произойти deadlock,
        # в случае если при полностью заполненной очереди/стэке
        # блокировку получит поток на запись.
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()

    def get(self) -> Any:
        with self.consumer_lock:
            if self.queue.qsize() > 0:
                return self.queue.get()
            else:
                return None

    def put(self, item) -> None:
        with self.producer_lock:
            while self.maxsize == self.queue.qsize():
                time.sleep(0.0001)
            self.queue.put(item)


class Producer:
    def __init__(self, name: str, buffer: BoundedBuffer, event: Event):
        self.buffer = buffer
        self.event = event
        self.message = 1
        self.name = name

    def work(self):
        # Работаь пока event == False
        while not self.event.is_set():
            self.buffer.put(f'{self.name}: {self.message}')
            print(f'{self.name} put {self.message}')
            self.message += 1
            time.sleep(0.0001)
        print(f'{self.name} work is done')


class Consumer:
    def __init__(self, name: str, buffer: BoundedBuffer, event: Event):
        self.buffer = buffer
        self.event = event
        self.name = name

    def work(self):
        # Работаь пока event == False
        while not self.event.is_set() or not self.buffer.queue.empty():
            message = self.buffer.get()
            print(f'{self.name} got {message}')
            time.sleep(0.0001)
        print(f'{self.name} work is done')


buffer = BoundedBuffer(10)
with ThreadPoolExecutor(max_workers=101) as executor:
    for a in range(1, 30):
        entity = Producer(f'prod-{a}', buffer, event)
        executor.submit(entity.work)
    for a in range(1, 70):
        entity = Consumer(f'cons-{a}', buffer, event)
        executor.submit(entity.work)
    # Подождать 5 секунд пока работают вызванные потоки.
    time.sleep(5)
    # Установить событие в True. При его проверке потоки изменят своё поведение.
    event.set()
