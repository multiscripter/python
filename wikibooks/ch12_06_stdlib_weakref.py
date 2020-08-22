import gc

import weakref # Поддержка слабых ссылок и слабых словарей.
# https://docs.python.org/3/library/weakref.html
# Source code: https://github.com/python/cpython/tree/3.8/Lib/weakref.py

# Модуль weakref позволяет создавать слабые ссылки на объекты.

# class weakref.ref(object[, callback])              # Создаёт слабую ссылку на оъект.
# class weakref.WeakKeyDictionary([dict])
# class weakref.WeakValueDictionary([dict])
# class weakref.WeakSet([elements])
# class weakref.WeakMethod(method)
# class weakref.finalize(obj, func, *args, **kwargs)

class A:
	def __init__(self, value):
		self.value = value

	def __repr__(self):
		return f'{{value: {self.value}}}'

a = A(10) # Обычная ссылка.
weakDict = weakref.WeakValueDictionary() # Словарь, использующий слабые ссылки (указатели).
weakDict['keyA'] = a                     # Поместить в словарь указатель на ссылку.
print(weakDict['keyA']) # {value: 10}

del a        # Удалить ссылку.
gc.collect() # Собрать мусор.

try:
	print(weakDict['keyA']) # Ошибка. Пустой указатель.
except KeyError as ex:
	print('No value mapped by key')