# -- 6.6. Организация циклов. ---
d1 = {'one': 1, 'two': 2}
result = []
for k, v in d1.items():
    result.append(f'{k}: {v}')
print(', '.join(result))  # one: 1, two: 2

result.clear()
for i, v in enumerate(['tic', 'tac', 'toe']):
    result.append(f'{i}: {v}')
print(', '.join(result))  # 0: tic, 1: tac, 2: toe

result.clear()
qz = ['q1', 'q2', 'q3']
az = ['a1', 'a2', 'a3']
for q, a in zip(qz, az):
    result.append(f'{q}: {a}')
print(', '.join(result))  # q1: a1, q2: a2, q3: a3

a = [1, 2, 3]
print(a)
result.clear()
for i in reversed(a):  # reversed(n) возвращает итератор.
    result.append(str(i))
print(', '.join(result))  # 3, 2, 1

print(sorted(['tic', 'tac', 'toe']))  # ['tac', 'tic', 'toe']
