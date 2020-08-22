from decimal import * # Реализация спецификации общей десятичной арифметики.
# https://docs.python.org/3/library/decimal.html
# Source code: Source code:

# Модуль «decimal» обеспечивает поддержку быстрой арифметики 
# с правильно округленным десятичным числом с плавающей запятой. 
# Он предлагает несколько преимуществ по сравнению с типом данных float.

# Например, вычисление 5%-ного налога на 70 копеечный телефонный счет 
# даёт различные результаты при использовании десятичной и двоичной арифметик.
print('0.7 * 1.05 =', 0.7 * 1.05)
print('Decimal("0.7") * Decimal("1.05") =', Decimal('0.7') * Decimal('1.05'))
print('Decimal(0.7) * Decimal(1.05) =', Decimal(0.7) * Decimal(1.05))
print()
print('1.1 + 2.2 =', 1.1 + 2.2) # 3.3000000000000003
print(Decimal('1.1') + Decimal('2.2')) # 3.3
print('getcontext().prec:', getcontext().prec)
print(Decimal(1.1) + Decimal(2.2)) # 3.300000000000000266453525910
print('getcontext().prec = 3')
getcontext().prec = 3
print(Decimal(1.1) + Decimal(2.2)) # 3.30