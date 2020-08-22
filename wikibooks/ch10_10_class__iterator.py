str = 'abc'
# Получить объект итератора.
itr = iter(str) 
# Передать оъект в функцию next()
print(next(itr)) # a
print(next(itr)) # b
print(next(itr)) # c

print('')

class MyClass:
	def __init__(self):
		self.x = 10
		self.y = 20
		self.z = 30

	def getProp(self, propName):
		return getattr(self, propName)

obj = MyClass()

for a in obj.__dict__:
	print(getattr(obj, a))

print('')

# Добавление возможности итерирования к классу.
# Определите метод __iter__(), который возвращает объект с методом next(). 
# Если класс определяет и метод next(), тогда __iter__() может просто возвращать self.
class Reverse:
	'Итератор по последовательности в обратном направлении'

	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index -= 1
		return self.data[self.index]

for char in Reverse('спам'):
	print(char)