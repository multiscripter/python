# Функция, возвращающая генератор (разновидность итератора).
def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]

# Варианты 1 и 2 имеют одинаковый результат.

# Вариант 1.
obj = reverse('гольф')
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

# Вариант 2.
for char in reverse('гольф'):
	print(char)