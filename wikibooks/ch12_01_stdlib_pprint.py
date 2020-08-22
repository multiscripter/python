import pprint # Симпатичный вывод данных.
# https://docs.python.org/3/library/pprint.html#module-pprint
# Source code: https://github.com/python/cpython/tree/3.8/Lib/pprint.py

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(stuff)