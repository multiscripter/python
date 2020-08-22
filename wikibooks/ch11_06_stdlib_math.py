import math # Mathematical functions (sin() etc.).
# https://docs.python.org/3/library/math.html#module-math

# Этот модуль обеспечивает доступ к математическим функциям, определенным стандартом C.

# В это скрипте предствлены не все фунции, объекты и их методы.

print('--- Constants ---')
print('math.pi:', math.pi)
print('math.e:', math.e)
print('math.tau:', math.tau)
print('math.inf:', math.inf)
print('math.nan:', math.nan)

print()

print('math.ceil(1.5):', math.ceil(1.5)) # 2
print('math.fabs(147334):', math.fabs(147334)) # 147334.0
print('math.factorial(10):', math.factorial(10)) # 3628800
print('math.floor(1.5):', math.floor(1.5)) # 1
# Остаток от деления. Может не совпадать с результатом a % b
print('math.fmod(11, 3):', math.fmod(11, 3)) # 2.0
print('math.frexp(16):', math.frexp(16)) # (0.5, 5)
# Для дробных чисел вычисляет сумму более точно, чем функция sum()
print('math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]):', 
		math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
) # 1.0
print('math.log(1024, 2):', math.log(1024, 2)) # 10.0

# Несколько примеров.
print('math.cos(math.pi / 4):', math.cos(math.pi / 4)) # 0.7071067811865476