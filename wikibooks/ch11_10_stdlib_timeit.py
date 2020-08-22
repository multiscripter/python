import timeit # Измерьте время выполнения небольших фрагментов кода.
# https://docs.python.org/3/library/timeit.html#module-timeit

# Какая инструкция выполняется быстрее.
print(timeit.timeit('char in text', setup='text = "sample string"; char = "g"'))
print(timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"'))

# Возвращает объект класса Timer.
t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
print(t.timeit())
print(t.repeat())