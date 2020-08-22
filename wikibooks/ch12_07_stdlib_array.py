from array import array # Эффективные массивы числовых значений.
# https://docs.python.org/3/library/array.html

arr = array('i', [1, 2, 3, 4, 5, 6]) # Создаёт экземпляр класса Array типа int.
print('arr.itemsize:', arr.itemsize) # Размер одного элемнета массива в байтах.
arr.append(10)

# array.count(x)
# Вернуть количество вхождений x в массиве.
print('arr.count(5)', arr.count(5)) # 1
print(arr[5]) # 6