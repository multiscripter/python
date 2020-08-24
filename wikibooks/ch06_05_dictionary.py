# --- 6.5. Словарь (Dictionary). ---
# Структура данных типа Key-Value Map.

# Создание.
# Вариант 1.
d = {}  # Пустой.
print(d)  # {}
d = {'one': 1, 'two': 2}  # Непустой.
print(d)  # {'one': 1, 'two': 2}
# Вариант 2.
d = dict([('one', 1), ('two', 2)])
print(d)  # {'one': 1, 'two': 2}
# Вариант 3 (если ключи - это строки).
d = dict(one=1, two=2)
print(d)  # {'one': 1, 'two': 2}

d['some'] = 'Foo'
print(d)  # {'one': 1, 'two': 2, 'some': 'Foo'}

print(d['one'])  # 1
print(d.get('one'))  # 1

del d['two']
print(d)  # {'one': 1, 'some': 'Foo'}

d['awesome'] = 'Bar'
print(d)  # {'one': 1, 'some': 'Foo', 'awesome': 'Bar'}
print(list(d.keys()))  # ['one', 'some', 'awesome']
print(sorted(list(d.keys())))  # ['awesome', 'one', 'some']

# Проверка наличия ключа.
print('one' in d)  # True
print('ten' in d)  # False

print(list(d.values()))  # [1, 'Foo']

# Сборщики словаря.
d = {x: x**2 for x in (2, 4, 6)}
print(d)  # {2: 4, 4: 16, 6: 36}
