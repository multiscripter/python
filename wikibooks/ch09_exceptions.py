from sys import exit

def divide(a, b):
	return a / b

# Пользовательское исключение.
class MyException(Exception):
	def __str__(self):
		return 'MyException raised'

while True:
	try:
		a = input('Enter first number > ')
		b = input('Enter second number > ')

		if a == '0' and b == '0':
			raise MyException()

		if a == 'q' or b == 'q':
			exit(0)

		a = float(a)
		b = float(b)
		
		print(divide(a, b))

	except OverflowError:
		print('Error: Too large number.')
		exit(1)

	except ZeroDivisionError as ex:
		print('Error: Division by zero.')
		print(type(ex)) # <class 'ZeroDivisionError'>
		# Неявный вызов метода __str__()
		print(ex)       # float division by zero
		exit(1)

	except ValueError:
		print('Error: Incorrect number entered.')
		exit(1)

	except (RuntimeError, TypeError):
		print('Error. RuntimeError or TypeError.')
		exit(1)
		# Прокинуть исключение наверх.
		raise

	except Exception as ex:
		print('except Exception as ex')
		print(type(ex))
		print(ex)

	# Перехват всех оставшихся типов исключений.
	except:
		print('Error. All other error types.')
		exit(1)

	# Этот блок выполняется если не выброшено ни одного исключения.
	else:
		print('There are no exceptions.')

	finally:
		print('Print this in any cases.')

# Аналог try-with-resources:
# Открытый ресурс будет закрыт в любом случае.
# Функция автозакрытия объекты ресурсов описана в их доках.

# with open("myfile.txt") as f:
#     for line in f:
#         print(line)