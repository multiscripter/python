import asyncio

# Защита от запроса на отмену задачи (Task.cancel()).
# Task.cancel() не гарантирует, что задача будет отменена.
# Полное подавление отмены не является распространенным явлением
# и активно не рекомендуется.


# Нихрена не рабоатет. Либо не отменяет, либо не защищает от отмены!


async def do_something(name: str):
    await asyncio.sleep(5)
    print(f'I am {name}')


async def do_something_runner():
    task1 = asyncio.create_task(do_something('task-1'))
    task2 = asyncio.shield(asyncio.create_task(do_something('task-2')))
    await asyncio.sleep(0.1)
    try:
        await task1
        task1.cancel()
    except asyncio.CancelledError:
        print('task-1 is cancelled')
    try:
        await task2
        task2.cancel()
    except asyncio.CancelledError:
        print('task-2 is cancelled')

asyncio.run(do_something_runner())
