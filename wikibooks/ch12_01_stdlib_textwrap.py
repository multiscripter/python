import textwrap # Перенос текста и заполнение.
# https://docs.python.org/3/library/textwrap.html#module-textwrap
# Source code: https://github.com/python/cpython/tree/3.8/Lib/textwrap.py

doc = """The textwrap module provides some convenience functions, 
as well as TextWrapper, the class that does all the work. 
If you’re just wrapping or filling one or two text strings, 
the convenience functions should be good enough; otherwise, 
you should use an instance of TextWrapper for efficiency."""

# width - ширина колонки.
# Возвращает список строк длиной не более width.
print('textwrap.wrap(doc, width = 40):')
print(textwrap.wrap(doc, width = 40))
print()

# Возвращает строку, разбитую символами \n на расстоянии не более width.
print('textwrap.fill(doc, width = 40):')
print(textwrap.fill(doc, width = 40))
print()

# Вовзращает начальный кусок текста длиной width с placeholder в конце.
# textwrap.shorten(text, width, placeholder = '. . .')
print(textwrap.shorten(doc, 100, placeholder = '<read more>'))
print()

# Удаляет пробелы из начала строк чтобы выровнять по левому крвю.
print(textwrap.dedent("""
	The textwrap module provides some convenience functions,
	as well as TextWrapper, the class that does all the work.
"""))
print()

print('textwrap.indent(doc, '	'):')
print(textwrap.indent(doc, '	'))