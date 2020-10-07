import threading
import time


def something(name: str):
    print(f'thread {name} is started. Waiting 1 second.')
    time.sleep(0.5)
    print(f'thread {name} is finished.')


# Создать поток и выполнить в ней функцию something().
t = threading.Thread(target=something, args=('Foo',))
# Запустить выполнение нового потока.
t.start()
# Вызывающему потоку дождаться выполнения нового потока.
t.join()
print('After t.start()')

# Без вызова t.join() вызывающщий поток завершит
# выполение раньше вызываемого и вывод будет такой:
# thread Foo is started. Waiting 1 second.
# After t.start()
# thread Foo is finished.

# При вызове t.join() вызывающщий поток дождётся завершения работы
# вызываемого потока и вывод будет такой:
# thread Foo is started. Waiting 1 second.
# thread Foo is finished.
# After t.start()
