import re # Regular expression operations.
# https://docs.python.org/3/library/re.html#module-re
# Source code: https://github.com/python/cpython/tree/3.8/Lib/re.py

# Этот модуль предоставляет операции сопоставления регулярных выражений, 
# аналогичные тем, что есть в Perl.

# В это скрипте предствлены не все фунции, объекты и их методы.

# --- Использование объекта регулярного выражения ---
print('--- Using a regular expression object ---')
print()

# Возвращает объект RegExp
# https://docs.python.org/3/library/re.html#re-objects
reObj = re.compile('py', re.I)

# Pattern.search(string[, pos[, endpos]])
# Просканируйте строку в поисках первого места, в котором это регулярное выражение 
# дает совпадение, и возвращается соответствующий объект совпадения.
print("reObj.search('I use Python'):", reObj.search('I use Python')) # <_sre.SRE_Match object; span=(6, 8), match='Py'>
print()

# Pattern.match(string[, pos[, endpos]])
# Если этому регулярному выражению соответствует ноль или более 
# символов В НАЧАЛЕ СТРОКИ, то возвращается соответствующий 
# 'объект соответствия' (https://docs.python.org/3/library/re.html#match-objects).
print("reObj.match('I use Python'):", reObj.match('I use Python')) # None
print()

# Pattern.fullmatch(string[, pos[, endpos]])
# Если ВСЯ СТРОКА соответствует этому регулярному выражению, 
# возвращается соответствующий объект соответствия. Иначе возвращается None
print("reObj.fullmatch('I use Python'):", reObj.fullmatch('I use Python')) # None
print("reObj.fullmatch('Py'):", reObj.fullmatch('Py')) # <_sre.SRE_Match object; span=(0, 2), match='Py'>
print()

# Pattern.split(string, maxsplit=0)
# Разделяет строку, используя шаблон как разделитель.
print("reObj.split('I use Python'):", reObj.split('I use Python')) # ['I use ', 'thon']
print()

# --- Использование функций ---
print('--- Using functions ---')
print()

pattern = 'со'
st = 'Союз Советских Социалистических Республик'

# re.search(pattern, string, flags=0)
# Просканируйте строку в поисках первого места, где шаблон регулярного 
# выражения дает совпадение, и возвращается соответствующий объект совпадения.
print('re.search(pattern, st, re.I):', re.search(pattern, st, re.I))  # <_sre.SRE_Match object; span=(0, 2), match='Со'>
print()

# re.match(pattern, string, flags=0)
# Если ноль или более символов В НАЧАЛЕ СТРОКИ соответствуют шаблону 
# регулярного выражения, возвращается соответствующий объект соответствия.
print('re.match(pattern, st, re.I):', re.match(pattern, st, re.I)) # <_sre.SRE_Match object; span=(0, 2), match='Со'>