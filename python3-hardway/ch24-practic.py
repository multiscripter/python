print("Попрактикуемся!")
print('Вывод бэкслэша \\')
print('\n символ\\n \tи символ \\t')

poem = """
\tДля счастья
мне.
Хочу\nтебя
я быть
\n\tникогда
"""

print("-----------------")
print(poem)
print("-----------------")

five = 10 - 2 + 3 - 6
print(f"10 - 2 + 3 - 6 = {five}")

def secret(start):
	jelly = start * 500
	jars = jelly / 1000
	crates = jars / 100
	return jelly, jars, crates # Возвращает кортеж.

point = 10000
beans, jars, crates = secret(point)

print("Изначально: {}".format(point))
print(f"Бобы {beans}, банки {jars}, ящики {crates}")

point /= 10
common = secret(point) # Возвращает кортеж.
print("Бобы {}, банки {}, ящики {}".format(*common))