import asyncio

# asyncio.wait() ожидает завершения Future и Coroutine, переданных в параметре.


async def foo() -> int:
    return 42


async def runner():
    task = asyncio.create_task(foo())
    done, pending = await asyncio.wait({task})
    if task in done:
        print('task is done')

asyncio.run(runner())
