import asyncio
from asyncio import StreamReader
from asyncio import StreamWriter


async def server(reader: StreamReader, writer: StreamWriter) -> None:
    """
    Простой TCP эхо-сервер.
    :param reader: читатель потока.
    :param writer: писатель в поток.
    :return: None
    """

    # Ожидать данные. Прочитать 100 байт при поступлении данных.
    # Если количество байт не указано, то прочить до EOF.
    data = await reader.read(100)
    # Декодировать байты.
    message = data.decode()
    # Получить доступ к дополнительной информации о транспорте.
    # https://docs.python.org/3.8/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info
    addr = writer.get_extra_info('peername')
    print(f"Received {message!r} from {addr!r}")

    # Сформировать сообщение клиенту.
    response = f"Server handled: {message}"
    # Декодировать сообщение в байты.
    data = response.encode('utf-8')
    print(f"Sending: {response}")
    # Записать в поток байты сообщения.
    writer.write(data)
    # Ожидать, пока не станет возможным возобновить запись в поток.
    await writer.drain()
    print("Close writer stream")
    # Закрыть поток записи.
    writer.close()


async def runner(server):
    # Запустить сервер сокетов и получить coroutine.
    server = await asyncio.start_server(server, '127.0.0.1', 8888)
    # Получить имя первого сокета. Возвращает: ('127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        # Начать принимать соединения, пока coroutine не будет отменена.
        # Сервер будет закрыт при coroutine.cancel().
        await server.serve_forever()

asyncio.run(runner(server))
