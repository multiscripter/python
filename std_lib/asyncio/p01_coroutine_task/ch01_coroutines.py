import asyncio
import time

# Coroutines - это более обобщенная форма подпрограмм.
# Subroutines вводятся в одной точке и завершаются в другой.
# В Coroutines можно входить, выходить и возобновлять их в самых разных точках.
# Их можно реализовать с помощью оператора async def.


async def hello_world(what: str):
    print('hello')
    # await можно применять только внутри функцией/методов.
    await asyncio.sleep(1)
    print(what)


# Простой вызов сопрограммы не приведет к ее выполнению:
# hello_world() # RuntimeWarning: coroutine 'hello_world' was never awaited.

# Для запуска coroutine asyncio предоставляет три основных механизма:
# 1. Метод asyncio.run() для явного запуска.
asyncio.run(hello_world('just run asyncio.run()'))


# 2. Запуск из функции/метода (по сути то же, что и механизм 1).
async def hello_world_runner():
    await hello_world('run inside function')
asyncio.run(hello_world_runner())


# 3. Функция asyncio.create_task() для одновременного запуска coroutines
# как asyncio Tasks (от части то же, что и механизм 2).
async def hello_task_world_runner():
    # Python 3.7+
    task1 = asyncio.create_task(hello_world('task1'))
    # All Python versions (low-level)
    task2 = asyncio.ensure_future(hello_world('task2'))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")
asyncio.run(hello_task_world_runner())
