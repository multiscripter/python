from sys import argv

script, fileName = argv

def printLine(file, line):
	print(line, file.readline(), end = '')

txt = open(fileName)
line = 1

printLine(txt, line)
line += 1
printLine(txt, line)
line += 1
printLine(txt, line)
line += 1
printLine(txt, line)

# Запуск python ch20-functions3.py ch17-copy-file-src.txt