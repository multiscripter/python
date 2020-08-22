import ch25_more_practic
from ch40_math_module import *
from ch40_class import Simple

print(f'ch25_more_practic.ch25var: {ch25_more_practic.ch25var}')
sentence = "Улыбок тебе дед Макар"
words = ch25_more_practic.breakStringBySpace(sentence)
print('words: ', words)

print('PI (ch40_math_module):', PI, 'Только 15 знаков после запятой. Обрезает 23.')
print('10 + 20 = ', add(10, 20))

obj = Simple('All roads go to Rome')
obj.printSlogan()
obj.apple()
obj.shout('Invaders must die!')
print(obj.slogan)
print(obj.__class__) # Содержит квалифицированное имя класса.
print(obj.__doc__) # Содержит документацию класса.