# --- 6.2. Оператор del. ---
a = [6, 5, 5, 4, 1, 11]
print(a)  # [6, 5, 5, 4, 1, 11]

del a[2]
print(a)  # [6, 5, 4, 1, 11]

# Удалить элементы с индексами с 1 до 3.
del a[1:3]
print(a)  # [6, 1, 11]

# Удалить все элементы.
del a[:]
print(a)  # []

# Удалить список.
del a
# print(a)  # NameError: name 'a' is not defined
