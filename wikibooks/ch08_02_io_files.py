txt = open('text.txt')

# a = txt.read() # Прочтёт весь файл.

for line in txt:
	print(line, end = '')

txt.seek(0) #  Переместить курсор в начало файла.
# https://docs.python.org/3/library/io.html?highlight=readlines#io.IOBase.readline
while True:
	line = txt.readline()
	if not line:
		break
	print(line, end = '')

txt.seek(0) #  Переместить курсор в начало файла.
# https://docs.python.org/3/library/io.html?highlight=readlines#io.IOBase.readlines
lines = txt.readlines()
print(lines)
print('Count lines:', len(lines))

txt.seek(100, 0) # передвинуть курсор на 100 от начала файла.
# Значение 0 параметра откуда отмеряет смещение от начала файла, 
# Значение 1 применяет текущую позицию в файле
# Значение 2 в качестве точки отсчёта использует конец файла. 
print(txt.readline())
print(txt.tell()) # 145 -текущая позиция курсора в файле.

# Запись в файл.

wtxt = open('write.txt', 'w')
print(wtxt.write('This is a test\n')) # 15 - количество записанных байтов.

# Чтобы записать в файл нечто отличное от строки, 
# предварительно это нечто нужно в строку сконвертировать
value = ('answer', 42)
s = str(value)
print(wtxt.write(s))

# Закрываем файлы (освобождаем ресурсы).
txt.close()
wtxt.close()

# Конструкция with аналогична try-with-resources в Java.
# Возможность автозакрытие ресурсов нужно смотреть в API объектов.
with open('text.txt') as f:
	l1 = f.readline()
print(l1, end = '')