import locale # Сервисы интернационализации.
# https://docs.python.org/3/library/locale.html#module-locale
# Source code: https://github.com/python/cpython/tree/3.8/Lib/locale.py

# Модуль locale открывает доступ к базе данных и функциям POSIX locale. 
# Механизм локали POSIX позволяет программистам решать определенные 
# культурные проблемы в приложении (например представление чисел, дат), 
# не требуя от программиста знания всех особенностей каждой страны, 
# в которой выполняется программное обеспечение.

x = 786495786475673456

print(locale.getdefaultlocale())
print()
print(locale.localeconv())
print()
print(locale.format("%d", x, grouping=True))
print()
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
print(locale.localeconv())
print()
print(locale.format("%d", x, grouping=True))