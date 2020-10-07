from concurrent.futures.thread import ThreadPoolExecutor
import time

# Более наглядная демонстрация работы многопоточности.


def fibonacci(name: str, end: int) -> None:
    start = cur = 1
    print(f'from {start} to {end}')
    while cur < end:
        print(f'{name}: {cur}')
        nxt = start + cur
        start = cur
        cur = nxt
        # Заснуть, тем самым дав другим потокам поработать.
        time.sleep(0.05)


# threads = []
# for a in range(1, 4):
#     t = threading.Thread(target=fibonacci, args=(f'Thread-{a}', 300))
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()

# Создать пул из трёх потоков.
# ThreadPoolExecutor сам распределит переданные в отображении функции по потокам.
with ThreadPoolExecutor(max_workers=3) as executor:
    names = [f'Thread-{a}' for a in range(1, 4)]
    # Выполнить функцию fibonacci трижды (можно и больше).
    executor.map(fibonacci, names, [300, 300, 300])
    # ThreadPoolExecutor вызывает Thread.join() неявно.
