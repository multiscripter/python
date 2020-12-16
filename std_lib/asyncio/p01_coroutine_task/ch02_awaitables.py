import asyncio

# Мы говорим, что объект является awaitable (ожидаемым) объектом,
# если его можно использовать в выражении await.
# Многие API-интерфейсы asyncio предназначены для приёма awaitable-объектов.

# Есть три основных типа awaitable-объектов: Coroutine, Task и Future.

# 1. Coroutine.
# coroutines являются awaitable, и поэтому их можно "ожидать" из других coroutines:
async def nested():
    return 42


async def run_nested():
    print(await nested())
asyncio.run(run_nested())


# 2. Task.
# Tasks используются для планирования запуска coroutines одновременно.
async def run_task_nested():
    task = asyncio.create_task(nested())
    print(await task)
asyncio.run(run_task_nested())


# 3. Future.
# Future - это специальный низкоуровневый ожидающий объект,
# представляющий конечный результат асинхронной операции.
# Когда ожидается объект Future, это означает, что coroutine будет ждать,
# пока Future не будет разрешен (resolved) в каком-то другом месте.
# Future-объекты в asyncio необходимы, чтобы разрешить использование кода
# на основе callback с async/await.
