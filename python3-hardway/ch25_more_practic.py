ch25var = 'Тестовая переменная из модуля ch25_more_practic';

def breakStringBySpace(st):
	return st.split(' ')

def sortWords(words):
	return sorted(words)

def getFirstWord(words):
	return words.pop(0)

def getLastWord(words):
	return words.pop(-1)

# Запуск.
# 1. python
# 2. import ch25_more_practic
# 3. sentence = "Улыбок тебе дед Макар"
# 4. words = ch25_more_practic.breakStringBySpace(sentence)
# 5. ch25_more_practic.sortWords(words)
# 6. ch25_more_practic.getFirstWord(words)
# 7. ch25_more_practic.getLastWord(words)

# Если импортировать так, то не придётся указывать имя модуля перед именем функции:
# from ch25_more_practic import *

# То есть вызов: имя_модуля.имя_функции([аргументы])

# Автоматическая справка (в интерактивном режиме).
# по модулю: help('ch25_more_practic')
# по функции: help('ch25_more_practic.breakStringBySpace')