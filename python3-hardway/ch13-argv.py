from sys import argv # Импортировать argv из модуля sys
script, first,  second, third = argv # Присвоить значения аргументов вызова в соответствующие переменные.
print("Этот скрипт называется ", script)
print("Первый аргумент вызова: ", first)
print("Второй аргумент вызова: ", second)
print("Третий аргумент вызова: ", third)

# Вызывать; python ./ch13-argv.py aaa bbb ccc