# https://webdevblog.ru/vvedenie-v-potoki-v-python/#race-conditions
import time
from concurrent.futures.thread import ThreadPoolExecutor

# Условия гонки (Race Conditions).
# Конкретно для этой задачи достигается тем,
# что перед присвоением нового значения нужно вызывать time.sleep()
# Если между получение значения счётчика и присвоением обновлённого значения
# не вызывать time.sleep(), то гонок не наблюдается (но это не означает,
# что оно не может возникнуть!).


class Counter:
    def __init__(self):
        self.value = 0

    def get_value(self) -> int:
        return self.value

    def set_value(self, value) -> None:
        self.value = value


class Incrementer:
    def __init__(self, name: str, counter: Counter):
        self.name = name
        self.c = counter

    def do(self):
        value = self.c.get_value()
        value += 1
        time.sleep(0.05)
        self.c.set_value(value)
        print(f'{self.name}: {self.c.value}')


class Decrementer:
    def __init__(self, name: str, counter: Counter):
        self.name = name
        self.c = counter

    def do(self):
        value = self.c.get_value()
        value -= 1
        time.sleep(0.01)
        self.c.set_value(value)
        print(f'{self.name}: {self.c.value}')


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

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(runner, modifiers)

print(f'counter.value: {counter.value}')
