# Базовая синхронизация с использованием блокировки
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor


class Counter:
    def __init__(self):
        self.count = 0
        self.value = 0
        self.lock = threading.Lock()

    def update(self, name: str, op: str) -> None:
        # Конструкция with lock позволяет всем потокам весеть на мониторе
        # и ожидать уведомления о разблокировке. Аналог notifyAll() из Java.
        # При выходе из блока блокировка монитора снимается и
        # висящие потоки уведомляются об этом событии.
        with self.lock:
            if op == '+':
                self.value += 1
            elif op == '-':
                self.value -= 1
            self.count += 1
            print(f'{name}: {self.value}')
            time.sleep(0.0001)


def runner(counter: Counter, name: str, op: str):
    for a in range(100):
        counter.update(name, op)


counter = Counter()
start_time = time.time()
with ThreadPoolExecutor(max_workers=100) as executor:
    for a in range(1, 101):
        op = '+' if not a % 2 else '-'
        executor.submit(runner, counter, f'Thread-{a}', op)
print(time.time() - start_time)
print(f'counter.value: {counter.value}')
print(f'counter.count: {counter.count}')
