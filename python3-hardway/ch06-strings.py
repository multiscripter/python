types = 10
x = f"Существует {types} типов людей."
lang = "Python"
do_not = "нет"
y = f"Те, кто понимает {lang}, и те, кто - {do_not}."

print(x)
print(y)

print(f"Я сказал: {x}")
print(f'А ещё я сказал: "{y}"')

h = False
joke = "Разве это не смешно?! {}";
print(joke.format(h))

left = "Python "
right = "way!"
print(left + right)