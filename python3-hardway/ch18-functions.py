def print_two(*args):
	arg1, arg2 = args
	print("*args - переменное число аргументов")
	print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Владимир", "Путин")
# print_two("Владимир", "Путин", "Великий") # Ошибка. too many values to unpack (expected 2)

def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

print_two_again("Владимир", "Путин")

def print_none():
	print("Эта функция не имеет параметров")
print_none()