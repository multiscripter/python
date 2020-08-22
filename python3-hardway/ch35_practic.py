from sys import exit

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

print('Калькулятор. Для выхода введите q')
while True:
	a = input('Введите первый операнд: ')
	b = input('Введите второй операнд: ')
	op = input('Введите оператор (один из +, -, *, /): ')

	# Вариант 1.
	#if a == 'q' or b == 'q' or op == 'q':
	# Вариант 2.
	if 'q' in a or 'q' in b or 'q' in op:
		exit(0)

	a = int(a)
	b = int(b)

	if op == '+':
		result = add(a, b)
	elif op == '-':
		result = subtract(a, b)
	elif op == '*':
		result = multiply(a, b)
	elif op == '/':
		result = divide(a, b)

	print(f'{a} {op} {b} = {result}')