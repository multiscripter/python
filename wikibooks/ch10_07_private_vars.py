# В Python нет модификаторов доступа к атрибутам и методам класса!

# Именование атрибутов класса __имяАтрибута введено для исключения конфликта одинаковых имён в иерархиях классов.
class UnderscorePriv:

	def __init__(self):
		self.__privateProp = 'Init underscore prop value'

	def getPrivateProp(self):
		return self.__privateProp

print('Using underscore naming:');
under = UnderscorePriv()
# print(under.__privateProp) # Да, тут ошибка. Но следующая инструкция просто затрёт существующую переменную.
print('print(under.getPrivateProp()):', under.getPrivateProp())
under.__privateProp = 'New private underscore prop value !!!!!!!'
print('print(under.__privateProp):', under.__privateProp)
print('print(under.getPrivateProp()):', under.getPrivateProp())

print('\n')

# Приватность на замыканиях.
class ClosPriv:
	def __init__(self):
		privateProp = None

		def getPrivateProp():
			return privateProp

		self.getPrivateProp = getPrivateProp

		def setPrivateProp(val):
			# Нужжно объявить nonlocal. Иначе при записи будет создана локальная переменная.
			nonlocal privateProp
			privateProp = val

		self.setPrivateProp = setPrivateProp

print('Using closures:');
obj2 = ClosPriv()
print('obj2.getPrivateProp():', obj2.getPrivateProp())
obj2.setPrivateProp('Ololo')
print('obj2.getPrivateProp():', obj2.getPrivateProp())

# print(obj2.privateProp) # AttributeError: 'ClosPriv' object has no attribute 'privateProp'
obj2.privateProp = 100
print(obj2.privateProp)

print('obj2.getPrivateProp():', obj2.getPrivateProp())

print('\nOther shit:')
# Ещё попытки эмулировать сокрытие данных.
class Test:
	def __init__(self, val):
		privateProp = val

	def getPrivateProp(self):
		return self.privateProp

	def setPrivateProp(self, val):
		self.privateProp = val

	def __get__(self, obj, type = None):
		raise AttributeError("'{}' object has no attribute '{}'".format(obj, self.attribute))

	def __set__(self, obj, value):
		raise AttributeError("'{}' object has no attribute '{}'".format(obj, self.attribute))

obj = Test(100)
# print(obj.__privateProp) # AttributeError: 'Test' object has no attribute '__privateProp'
print(Test) # <class '__main__.Test'>

obj.privateProp = 68763487534 # Таки присваивает !!!
# print(obj.privateProp) # AttributeError: 'Test' object has no attribute 'privateProp'

print(obj.getPrivateProp())