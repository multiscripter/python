from sys import argv

script, filename = argv

input(f"Нажмите Enter для стирания файла {filename}. Для выхода нажмите Ctrl + C")





print("Открываю файл", filename)
txt = open(filename, 'w')

# Character Meaning
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       open for exclusive creation, failing if the file already exists
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing). Например: r+, w+, a+
# 'U'       universal newlines mode (deprecated)

print("Очищаю файл", filename)
#txt.truncate() # Вызов truncate() не нужен, если файл открыт в режиме 'w'

print("Введите 4 строки для записи в файл")
l1 = input("Строка 1: ")
l2 = input("Строка 2: ")
l3 = input("Строка 3: ")
l4 = input("Строка 4: ")

print("Записываю в файл.")

txt.write(l1 + "\n" + l2 + "\n")
txt.write(l3)
txt.write("\n")
txt.write(l4)
txt.write("\n")

print("Закрываю файл.")
txt.close()

# Запуск: python ./ch16-write-file.py ch16-write-file.txt