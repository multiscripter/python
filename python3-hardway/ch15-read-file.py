from sys import argv

script, filename = argv

txt = open(filename) # Python позволяет открыть файл многократно и получить несколько объектов файла.

print("Содержимое файла", filename)
print(txt.read())
txt.close() # Явно закрыть дескриптор открытого файлы и освободить ресурс.

filename = input("\nВведите имя файла: ")
txt = open(filename)
print(txt.read())
txt.close() # Явно закрыть дескриптор открытого файлы и освободить ресурс.

# запуск: python ./ch15-read-file.py ch15-read-file.txt

# open(...)
#    open(name[, mode[, buffering]]) -> file object
#    
#    Открыть файл и вернуть соответствующий файловый объект.  This is the
#    preferred way to open a file.  See file.__doc__ for further information.

# https://docs.python.org/3.6/library/functions.html#open

# file object
#	An object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource.
