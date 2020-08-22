# Консервирование (Бинарная сериализация).
# https://ru.wikibooks.org/wiki/Python/%D0%A3%D1%87%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA_Python_3.1#%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_pickle

import pickle

class CStruct:
	pass

obj = CStruct()
obj.name = 'John'
obj.age  = 100

with open('ch08_02_02_pickle.txt', 'r+b') as f:
	pickle.dump(obj, f)
	f.seek(0)
	un = pickle.load(f)
	print(un.__dict__)