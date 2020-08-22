def havka(a, b):
	print(f"Сыра: {a}, чипсов: {b}");print("Погнали!")

print("Числовые константы могут быть аргументами функции")
havka(20, 30)

print("Переменные могут быть аргументами функции")
a1 = 10
a2 = 50
havka(a1, a2)

print("Выражения, возвращающие значения, могут быть аргументами функции")
havka(a1 + 20, 5 + 10)

def cp(src, dst):
	open(dst, 'w').write(open(src).read())

src = "ch17-copy-file-src.txt"
dst = "ch17-copy-file-dest.txt"
print(f"Функция cp(src, dst) копирует содержимое файла {src} в файл {dst}")
cp(src, dst)

val = 10
def changeArg(val):
	val += 10
	print("Внутри функции. Локальный val:", val)

changeArg(val)
print("val:", val)
