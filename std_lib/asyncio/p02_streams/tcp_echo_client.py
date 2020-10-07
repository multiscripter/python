import asyncio


async def tcp_echo_client(message: str):
    # Открыть соединение. Возвращает объекты читателя потока и писателя в поток.
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Send: {message!r}')
    # Записать в поток байты сообщения.
    writer.write(message.encode())

    # Ожидать данные. Прочитать 100 байт при поступлении данных.
    # Если количество байт не указано, то прочить до EOF.
    data = await reader.read(100)
    # Декодировать байты.
    print(f'Received: {data.decode()!r}')

    print('Close writer stream')
    # Закрыть поток записи.
    writer.close()

asyncio.run(tcp_echo_client('Message from simple TCP client'))
