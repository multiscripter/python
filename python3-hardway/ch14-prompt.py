from sys import argv

script, name = argv
prompt = '>'

print(f"Привет, {name}, я - скрипт {script}.")
print("Сколько тебе лет?")
age = input(prompt)

print(f"""
	{name}, тебе {age} лет.
	Пока!
""")

# Запуск: python ./ch14-prompt.py John