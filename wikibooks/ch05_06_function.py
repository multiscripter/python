# --- 5.6. Определение функций. ---
def fib(n):
    """Возвращает список чисел ряда Фибоначчи, ограниченный n."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

print(fib(100))

# --- 5.7.1. Значения аргументов по умолчанию. ---
def say(what='%nothing to say%'):
    print(what)
say('hello')
say()

# Значения по умолчанию вычисляются в месте определения функции,
# в определяющей области.
i = 5
def f(arg=i):
    print(arg)
i = 6
f()  # 5


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]

# --- 5.7.2. Именованные параметры. ---
def a(man, woman):
    print(f'{man} and {woman} are married')
a('John', 'Mary')
a(woman='Mary', man='John')

def printArgs(pos1, pos2, *nopos, **named):
    print('Позиционный параметр1: ' + pos1)
    print('Позиционный параметр2: ' + pos2)
    for arg in nopos:
        print(arg)
    for kw in named:
        print(kw, ":", named[kw])

printArgs('pos1', 'pos2', 'nopos1', 'nopos2', named1='named1', named2='named2')

# --- 5.7.3. Списки параметров произвольной длины. ---
def c(required1, requiredN, *optional):
    for a in optional:
        print(a)

c(1, 2, 'optional1', 'optional2', 'optionalN')

# Все параметры необязательные
# def funcName(*optional): . . .

# --- 5.7.4. Распаковка списков параметров. ---
# Обычный вызов.
print(list(range(0, 10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Распаковка.
args = [0, 10, 2]
print(list(range(*args)))  # [0, 2, 4, 6, 8]

analog = {
    'pos1':'pos1',
    'pos2':'pos2',
    'nopos': ['nopos1', 'nopos2'],
    'named': {'named1':'named1', 'named2':'named2'}
}
printArgs(**analog)

# --- 5.7.5. Модель lambda. ---
# https://webdevblog.ru/kak-ispolzovat-v-python-lyambda-funkcii/
d = (lambda x: x + 1)(2)
print(d)  # 3

# Ещё пример:
def simpleMathOps(f, a, b):
    return f(a, b)

print(simpleMathOps(lambda a, b: a + b, 20, 10))  # 30
print(simpleMathOps(lambda a, b: a - b, 20, 10))  # 10
print(simpleMathOps(lambda a, b: a * b, 20, 10))  # 200
print(simpleMathOps(lambda a, b: a / b, 20, 10))  # 2.0

# --- .5.7.6. Строки документации ---
def showDocFormat():
    """Не делаем ничего, но документируем.

    Нет, правда, эта функция ничего не делает.
    """
    pass

print(showDocFormat.__doc__)
