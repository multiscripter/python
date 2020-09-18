a = [1, 2, 3]
for n in a:
    if n < 4:
        continue
    if n == 4:
        print(f'В списке {a} найдено число 4')
        break
else:
    print(f'В списке {a} нет числа 4')

a.append(4)
for n in a:
    if n < 4:
        continue
    if n == 4:
        print(f'В списке {a} найдено число 4')
        break
else:
    print(f'В списке {a} нет числа 4')

z = 0
while z < len(a):
    if a[z] == 4:
        print(f'В списке {a} найдено число 4')
        break
    z += 1
else:
    print(f'В списке {a} нет числа 4')

# В Python нет лэйблов для break и continue.
# https://www.python.org/dev/peps/pep-3136/
# Пример выхода из всех циклов:
flag = False
for a in range(1, 5):
    print(f'outer: {a}')
    for b in range(1, 5):
        print(f'inner: {b}')
        if a == 3 and b == 3:
            flag = True
            break
    if flag:
        break
