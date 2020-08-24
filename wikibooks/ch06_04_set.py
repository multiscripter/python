# --- 6.4. Множество (Set). ---

# Создание.
# Вариант 1.
s1 = set([1, 2, 2, 3])
print(s1.__class__)  # <class 'set'>
print(s1)  # {1, 2, 3}
# Вариант 2.
s2 = {1, 2, 2, 3}
print(s2.__class__)  # <class 'set'>
print(s2)  # {1, 2, 3}

dict = {}  # Создаётся пустой словарь!
print(dict.__class__)  # <class 'dict'>

print(2 in s1)  # True
print(0 in s2)  # False

# Сборщики множеств.
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)  # {'r', 'd'}
