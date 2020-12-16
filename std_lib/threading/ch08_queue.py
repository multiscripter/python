# https://webdevblog.ru/vvedenie-v-potoki-v-python/#threading-objects

import time
from queue import Queue
from concurrent.futures.thread import ThreadPoolExecutor


queue = Queue(10)


def add(qu: Queue, t_num: int) -> None:
    for b in range(100):
        val = f'{t_num}-Foo-{b}'
        print(f'val: {val}')
        # Если в очереди нет места, то будет ждать пока оно появится.
        qu.put(val)
        time.sleep(0.0001)
        print(f'qsize: {qu.qsize()}')


def remove(qu: Queue) -> None:
    for b in range(100):
        got = qu.get()
        # Уведомить очередь, что манипуляции с ней законччены,
        # чтобы она могла снять блокировку и продолжить работу.
        qu.task_done()
        print(f'got : {got}')
        time.sleep(0.0001)


with ThreadPoolExecutor(max_workers=100) as executor:
    for a in range(50):
        executor.submit(add, queue, a)
    for a in range(50):
        executor.submit(remove, queue)

print(f'queue.qsize(): {queue.qsize()}')
