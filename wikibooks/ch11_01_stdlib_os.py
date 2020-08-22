# Взаимодействие с операционной системой.
import os # Miscellaneous operating system interfaces.
# https://docs.python.org/3/library/os.html#module-os
# Source code: https://github.com/python/cpython/tree/3.8/Lib/os.py
# Note All functions in this module raise OSError

# Лучше всего применять import os вместо from os import *. 
# Это предохранит встроенную функцию open() 
# от замещения функцией os.open(), имеющей несколько иное назначение.

print(os.name) # зарегистрированные имена: 'posix', 'nt', 'java'
print(os.getcwd()) # возвращает путь к текущему каталогу
print(os.ctermid()) # /dev/tty в Ubuntu.
print('os.environ:', os.environ) # Карта с переменными окружения.

print()
print('dir(os):', dir(os)) # список всех атрибутов модуля.
print()
# help(os) # страница руководства по модулю на основе строк документации

import shutil # High-level file operations, including copying.
# https://docs.python.org/3/library/shutil.html#module-shutil
# Source code: https://github.com/python/cpython/tree/3.8/Lib/shutil.py

# Return the file's destination.
# В доках API ошибка. Там указано, что у функции 4 параметра.
# shutil.copy(src, dst, follow_symlinks = True)
print(shutil.copy('text.txt', 'write.txt', follow_symlinks=False))

# Recursively copy an entire directory tree rooted at src to a directory named dst and return the destination directory.
# shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)