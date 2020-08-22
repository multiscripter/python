import random # Generate pseudo-random numbers with various common distributions.
# https://docs.python.org/3/library/random.html#module-random
# Source code: https://github.com/python/cpython/tree/3.8/Lib/random.py

# Этот модуль реализует генераторы псевдослучайных чисел для различных распределений.

# В это скрипте предствлены не все фунции, объекты и их методы.

# random.choice(seq)
# Вернуть случайный элемент из непустой последовательности seq. Если seq пуст, вызывает IndexError.
print("random.choice(['apple', 'pear', 'banana']):", random.choice(['apple', 'pear', 'banana']))

# random.sample(population, k)
# Возвращает список уникальных элементов длиной k, выбранных из последовательности или набора популяций.
print('random.sample(range(100), 10):', random.sample(range(100), 10))
# Возвращает список из трёх элементов.
print('random.sample([1, 2, 3, 4, 5],  3):', random.sample([1, 2, 3, 4, 5],  3))

# random.random()
# Вернуть следующее случайное число с плавающей запятой в диапазоне [0,0, 1,0).
print('random.random():', random.random())

# random.randrange(stop)
# random.randrange(start, stop[, step])
# Вернуть случайно выбранный элемент из диапазона (start, stop, step).
print('random.randrange(6):', random.randrange(6))