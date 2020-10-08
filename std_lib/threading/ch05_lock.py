# https://webdevblog.ru/vvedenie-v-potoki-v-python/#basic-synchronization-using-lock

# Базовая синхронизация с использованием блокировки
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor


class Counter:
    def __init__(self):
        self.count = 0
        self.value = 0
        self.lock = threading.Lock()

    def get_value(self) -> int:
        return self.value

    def set_value(self, value) -> None:
        self.value = value


class Incrementer:
    def __init__(self, name: str, counter: Counter):
        self.name = name
        self.c = counter

    def do(self):
        # Повиснуть на мониторе до тех пор,
        # пока блокировка не будет получена.
        self.c.lock.acquire()
        value = self.c.get_value()
        value += 1
        self.c.count += 1
        time.sleep(0.0001)
        self.c.set_value(value)
        print(f'{self.name}: {self.c.value}')
        # Освободить блокировку монитора.
        self.c.lock.release()


class Decrementer:
    def __init__(self, name: str, counter: Counter):
        self.name = name
        self.c = counter

    def do(self):
        # Повиснуть на мониторе до тех пор,
        # пока блокировка не будет получена.
        self.c.lock.acquire()
        value = self.c.get_value()
        value -= 1
        self.c.count += 1
        time.sleep(0.0001)
        self.c.set_value(value)
        print(f'{self.name}: {self.c.value}')
        # Освободить блокировку монитора.
        self.c.lock.release()


def runner(modifier):
    for a in range(100):
        modifier.do()


counter = Counter()
names = [f'Thread-{a}' for a in range(1, 101)]
modifiers = []
for a in range(1, 101):
    if not a % 2:
        modifiers.append(Incrementer(f'Thread-{a}', counter))
    else:
        modifiers.append(Decrementer(f'Thread-{a}', counter))
start_time = time.time()
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(runner, modifiers)
print(time.time() - start_time)
print(f'counter.value: {counter.value}')
print(f'counter.count: {counter.count}')
