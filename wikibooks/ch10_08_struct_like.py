# Эмуляция struct из языка C.
# Объявляем пустой класс, а потом просто пихаем значения в свойства через точку.
class CStruct:
    pass


st = CStruct()
st.name = 'John Doe'
st.age = 100
st.prgrammer = True

print(st.__dict__)  # {'name': 'John Doe', 'age': 100, 'prgrammer': True}
print(getattr(st, 'name'))  # John Doe
setattr(st, 'x', 100)
print(st.__dict__)  # {'name': 'John Doe', 'age': 100, 'prgrammer': True, 'x': 100}
delattr(st, 'x')
print(st.__dict__)  # {'name': 'John Doe', 'age': 100, 'prgrammer': True}
