people = 20
cats = 30

if people < cats:
	print("Мир спасён. Кошечек больше, чем людишек")
elif people > cats:
	print("Мир обречён")
else:
	print("Людишек и кошечек поровну. Мир на грани.")

print("Тернарный оператор в Python выглядит так: %expression_with_bool_result% if %on_true% else %on_false%")
print(people == cats if "Баланс" else "Нет баланса")
