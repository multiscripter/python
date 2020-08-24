print("Строка в двойных кавычках")
print("Строка в одинарных кавычках")

multu = 'Символ бэкслэш используется \
для переноса строк в коде'
print(multu)

raw = r'Символ r создаёт "сырую" строкой. '
raw += r'В такой строке спецсимолы типа \n или \t не конвертируются'
print(raw)

print('''
        Это  
        многострочный 
        итерал''')
print("""Это ещё один вид 
многострочного итерала""")

print('Строки ' + 'конкатенируются ' + 'символом ' + '+')
a = 'повторение'
print(a * 2)  # повторениеповторение
print('автоматическая ' 'конкатенация' ' строк')

str = 'Строка - это массив символов'
# Строки неизменяемы! Присваивание по индексу вызовет ошибку!
print(str[4])  # к
print(str[0:7])  # Строка
print(str[:7])  # Строка
print(str[20:])  # символов
print(str[-1])  # в
print(str[-2:])  # ов
print(str[:-22])  # Строка
# Выход за границы при обращениии к строкам как к срезам [N:N] - безопасен:
print(str[20:100])
print(str[100:101])
# Выход за границы при обращениии к строкам как к массивам [N] вызовет ошибку:
# print(str[100]) # IndexError: string index out of range
# print(str[-100]) # IndexError: string index out of range

print(f'Длина строки "{str}" : {len(str)} символов')

# Начиная с Python версии 3.0 строковый тип поддерживает только!

#  Пример вывода всяких символов:
print('\u0429\u0443\u043a\u0430')  # Щука
print('\u2660\u2661\u2662\u2663')  # Символы мастей игральных карт.
