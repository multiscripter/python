import logging # Гибкая система регистрации событий для приложений.
# https://docs.python.org/3/library/logging.html
# Source code: https://github.com/python/cpython/tree/3.8/Lib/logging/__init__.py

# Этот модуль определяет функции и классы, которые реализуют 
# гибкую систему регистрации событий для приложений и библиотек.

# logging.basicConfig(**kwargs)
# Именованные параметра: filename, filemode, format, datefmt, style, level, stream, handlers, force

# По умолчанию логирование ведётся в stderr. Переключим на логирование в файл. 
logging.basicConfig(filename = 'ch12_05_stdlib_logging.log', level = logging.DEBUG)

logging.debug('Отладочная информация')
logging.info('Для информации')
logging.warning('Предупреждение: файл %s не найден', 'server.conf')
logging.error('Произошла ошибка!')
logging.critical('Критическая ошибка - выход')