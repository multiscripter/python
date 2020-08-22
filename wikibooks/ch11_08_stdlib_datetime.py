import datetime # Basic date and time types.
# https://docs.python.org/3/library/datetime.html#module-datetime
# Source code: https://github.com/python/cpython/tree/3.8/Lib/datetime.py

# Модуль datetime предоставляет классы для управления датой и временем.

# Содержит несколько классов:
# timedelta, date, datetime, time, tzinfo, timezone.

# Класс date.
# Конструирует объект date по указанным параметрам.
print('datetime.date(2050, 12, 4):', datetime.date(2050, 12, 4)) # 2050-12-04

# Возвращает текущую дату в формате YYYY-MM-DD
print('datetime.date.today():', datetime.date.today())

# Конструирует объект date из Linux timestamp.
print(datetime.date.fromtimestamp(1598015269))

# Конструирует объект date из количества дней от роджества Христова.
print(datetime.date.fromordinal(100500))

# Python 3.7+
# Конструирует объект date из строки в ISO-формате.
# print(datetime.date.fromisoformat('2019-12-04'))

# Python 3.8+
#classmethod date.fromisocalendar(year, week, day)

# Class attributes:
print('datetime.date.min:', datetime.date.min) # 0001-01-01
print('datetime.date.max:', datetime.date.max) # 9999-12-31

# Наименьшая возможная разница между разными объектами даты, timedelta (days = 1).
print('datetime.date.resolution:', datetime.date.resolution) # 1 day, 0:00:00

#Instance attributes (read-only):
print('datetime.date.year:', datetime.date.year) # <attribute 'year' of 'datetime.date' objects>
print('datetime.date.month:', datetime.date.month) # <attribute 'month' of 'datetime.date' objects>
print('datetime.date.day:', datetime.date.day) # <attribute 'day' of 'datetime.date' objects>


# Примеры использования.
print()
print('Age in days:', datetime.date.today() - datetime.date(1980, 12, 4))
print('datetime.date.today().strftime("%d.%m.%Y"):', datetime.date.today().strftime("%d.%m.%Y"))