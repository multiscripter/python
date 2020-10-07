import asyncio


async def eternity(name: str) -> None:
    await asyncio.sleep(0.5)
    print(f'Wake up, {name}!')


async def runner() -> None:
    name: str = 'Foo'
    try:
        await asyncio.wait_for(eternity(name), timeout=0.5)
    except asyncio.TimeoutError:
        print(f'{name}, time is out.')

    # Защита от отмены не работает!
    name = 'Bar'
    try:
        # Если timeout < sleep, то eternity() всегда срабатывает.
        # Если timeout > sleep, то всегда выбрасывается исключение.
        # Если timeout == sleep, то eternity() срабатывает,
        # а затем выбрасывается исключение!
        await asyncio.wait_for(asyncio.shield(eternity(name)), timeout=0.5)
    except asyncio.TimeoutError:
        print(f'{name}, time is out.')

asyncio.run(runner())
