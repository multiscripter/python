print("Как тебя зовут?", end=' ') # второй параметр end = ' ' означает: вставить пробел в конце строки вместо символа \n
name = input()
print("Сколько тебе лет?", end=' ')
age = input()
print("Каков твой рост?", end=' ')
height = input()

print(f"Итак, {name}, тебе {age} лет и твой рост: {height}.")
print("\n")

name2 = input("Как тебя зовут? ") # В аргументе передаётся текст перед вводом.
print("Тебя зовут:", name2);

age2 = input("Сколько тебе лет? ")
age2 = int(age2) # Приведение типа Strng к Int
print("Через 10 лет тебе будет:", age2 + 10)

# Утилита pydoc %имя% выводит информацию о %имя%