from glob import * # Unix shell style pathname pattern expansion.
# https://docs.python.org/3/library/glob.html#module-glob
# Source code: https://github.com/python/cpython/tree/3.8/Lib/glob.py

# Модуль glob находит все пути, соответствующие заданному шаблону, 
# в соответствии с правилами, используемыми оболочкой Unix.

# Вернуть возможно пустой список имен путей, соответствующих имени пути, 
# который должен быть строкой, содержащей спецификацию пути.
# glob.glob(pathname, recursive=False)
names = glob('*.py')
for name in names:
	print(name)
print()

# Возвращает итератор, который дает те же значения, что и glob (), 
# без фактического сохранения их всех одновременно.
# glob.iglob(pathname, *, recursive=False)
names2 = iglob('*.py')
for name in names2:
	print(name)
print()

# Экранирует все специальные символы ('?', '*' И '[').
# glob.escape(pathname)
print(escape('aaa/?bbb/*ccc[ddd.ext')) # aaa/[?]bbb/[*]ccc[[]ddd.ext

# Шаблон для файлов, наичнающихся с точки (.htaccess и т. д.).
dot = glob('.*')
print(dot)