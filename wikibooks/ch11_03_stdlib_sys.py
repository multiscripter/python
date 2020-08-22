import sys # Access system-specific parameters and functions.
# https://docs.python.org/3/library/sys.html#module-sys
# Source code: 

# Этот модуль обеспечивает доступ к некоторым переменным, 
# используемым или поддерживаемым интерпретатором, а также к функциям, 
# которые сильно взаимодействуют с интерпретатором.

# Список аргументов командной строки, переданных скрипту Python. argv [0] - имя скрипта
print('sys.argv:', sys.argv)
print()
sys.stdout.write('sys.stdout.write()\n') # записать в stdout
sys.stderr.write('sys.stderr.write()\n') # записать в stderr
print()
print('sys.byteorder:', sys.byteorder)
print()
# Целое число, задающее максимальное значение, которое может принимать переменная типа Py_ssize_t. 
# Обычно это 2 ** 31-1 на 32-битной платформе и 2 ** 63-1 на 64-битной платформе.
print('sys.maxsize:', sys.maxsize)
print()
print('sys.modules:', sys.modules)
print()
print('sys.path:', sys.path)
print()
print('sys.platform:', sys.platform)
print()
# Именованный кортеж, содержащий информацию о реализации потока.
print('sys.thread_info:', sys.thread_info)
print()
print('sys.version:', sys.version)
sys.exit(0)