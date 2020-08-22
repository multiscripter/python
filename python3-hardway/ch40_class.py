class Simple(object):
	'This is my first class difinition.' # Документация класса.

	def __init__(self, slogan):
		self.slogan = slogan

	def printSlogan(self):
		print('Slogan:', self.slogan)

	def apple(self):
		print('I am a sweet apple!')

	# Вызвать нужно obj.shout('text')
	# Аргумент self интерпретатор передаёт неявно.
	def shout(self, words):
		print('Shout:', words)

# obj = Simple('All roads go to Rome')
# obj.apple()
# print(obj.slogan)