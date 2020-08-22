import reprlib # Alternate repr() implementation with size limits.
# https://docs.python.org/3/library/reprlib.html#module-reprlib
# Source code: https://github.com/python/cpython/tree/3.8/Lib/reprlib.py

# Модуль reprlib предоставляет средства для создания представлений объектов 
# с ограничениями на размер результирующих строк. Это используется 
# в отладчике Python и может быть также полезно в других контекстах.

replObj = reprlib.Repr()
replObj.maxlong = 50 # максимальное количество разрядов в представлении integer. Default: 40
replObj.maxother = 300
replObj.maxstring = 40 # максимальное количество символов в представлении строки. Default: 30
replObj.maxset = 500 # максимальное количество элементов Set в представлении. Default: 6
#print(replObj.__dict__)

print(replObj.repr(12345678901234567890123456789012345678901234567890))
print(replObj.repr('12345678901234567890123456789012345678901234567890')) # '12345678901234567...345678901234567890'

# Предстваление экземпляра Set.
print(replObj.repr(set('supercalifragilisticexpialidocious')))
#print(replObj.repr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
