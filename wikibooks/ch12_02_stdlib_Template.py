from string import Template
# https://docs.python.org/3/library/string.html#template-strings
# Source code: https://github.com/python/cpython/tree/3.8/Lib/string.py

# Строки шаблона обеспечивают более простые замены строк, как описано в PEP 292.

strPattern = "${subject} ${predicate} ${otherwords}${endSign}"
strTpl = Template(strPattern)

words = {
	'subject': 'I',
	'predicate': 'learn',
	'otherwords': 'Python',
	'endSign': '!'
}

# substitute(mapping={}, /, **kwds)
print(strTpl.substitute(words))
print(strTpl.substitute(subject='I', predicate='learn', otherwords='Python', endSign='!'))

# safe_substitute(mapping={}, /, **kwds)
print(strTpl.safe_substitute(subject='I', predicate='learn', endSign='!'))
print()
print('strTpl.template:', strTpl.template)