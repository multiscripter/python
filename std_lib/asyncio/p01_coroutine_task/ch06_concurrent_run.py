import asyncio

# Выполнение происходит по очереди А, В, С по одной итерации.


async def fibonacci(name: str,  end: int):
    start = cur = 1
    print(f'from {start} to {end}')
    while cur < end:
        print(f'{name}: {cur}')
        nxt = start + cur
        start = cur
        cur = nxt
        await asyncio.sleep(0.1)


async def fibonacci_runner():
    await asyncio.gather(
        fibonacci('A', 300),
        fibonacci('B', 150),
        fibonacci('C', 100)
    )

asyncio.run(fibonacci_runner())
