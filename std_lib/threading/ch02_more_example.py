import threading

# Более наглядная демонстрация работы многопоточности.


def fibonacci(name: str, end: int) -> None:
    start = cur = 1
    print(f'from {start} to {end}')
    while cur < end:
        print(f'{name}: {cur}')
        nxt = start + cur
        start = cur
        cur = nxt


threads = []
for a in range(1, 4):
    t = threading.Thread(target=fibonacci, args=(f'Thread-{a}', 300))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
