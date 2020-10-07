# Streams - это высокоуровневые примитивы с поддержкой async/await
# для работы с сетевыми подключениями. Потоки позволяют отправлять
# и получать данные без использования обратных вызовов
# или низкоуровневых протоколов и транспортов.
import asyncio

# Установает сетевое соединение и возвращает пару объектов (reader, writer).
# coroutine asyncio.open_connection(host=None, port=None, *, loop=None, limit=None,
# ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None,
# server_hostname=None, ssl_handshake_timeout=None)
# Пример вызова:
# reader, writer = asyncio.open_connection('127.0.0.1', 8888)

# Запускает сервер сокетов.
# coroutine asyncio.start_server(client_connected_cb, host=None, port=None, *,
# loop=None, limit=None, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE,
# sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None,
# ssl_handshake_timeout=None, start_serving=True)
# Пример вызова:
# server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

# asyncio.open_unix_connection(. . .)
# asyncio.start_unix_server(. . .)

# Класс asyncio.StreamReader.
# Представляет объект чтения, который предоставляет API для чтения данных
# из потока ввода-вывода.
# Не рекомендуется создавать экземпляры объектов StreamReader напрямую;
# используйте вместо них open_connection() и start_server().

# Класс asyncio.StreamWriter.
# Представляет объект записи, который предоставляет API для записи данных
# в поток ввода-вывода.
# Не рекомендуется создавать экземпляры объектов StreamWriter напрямую;
# используйте вместо них open_connection() и start_server().

