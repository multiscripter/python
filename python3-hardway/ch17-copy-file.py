from sys import argv
from os.path import exists

script, src, dest = argv

print(f"Копирование из файла {src} в файл {dest}")

srcFile = open(src)
data = srcFile.read()

print(f"Размер файла-источника (байт): {len(data)}")
print(f"Проверка существования файла: {exists(dest)}")
input("Нажмите Enter для продолжения или Ctrl + C для отмены")

destFile = open(dest, 'w')
destFile.write(data)

print("Копирование завершено.\nЗакрываю дескрипторы файлов.")

srcFile.close()
destFile.close()

print("Выхожу.")

# Запуск: python ./ch17-copy-file.py ch17-copy-file-src.txt ch17-copy-file-dest.txt

print("Одна строка кода")
open(dest, 'w').write(open(src).read())

print("\nНесколько строк кода можно записать в одну через ;")
srcFile = open(src);data = srcFile.read();destFile = open(dest, 'w');destFile.write(data);srcFile.close();destFile.close()