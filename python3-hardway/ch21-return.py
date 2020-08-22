def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

a = 10
b = 5
result = add(a, b)
print(f"{a} + {b} = {result}")
result = subtract(a, b)
print(f"{a} - {b} = {result}")
print(f"{a} * {b} = {multiply(a, b)}")
print(f"{a} / {b} = {int(divide(a, b))}")

print(divide(add(a, b), add(1.0, 2))) # Неявно приводит тип float