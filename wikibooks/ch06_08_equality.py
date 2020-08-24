# --- 6.8. Сравнение последовательностей и других типов. ---
st = 'Foo'
print(st == "F" + "oo")  # True

print([1, 2, 3] == list([1, 2, 3]))  # True
print((1, 2, 3) == tuple([1, 2, 3]))  # True
print({1, 2, 3} == set([1, 2, 3]))  # True
print({'one': 1, 'two': 2} == dict([('one', 1), ('two', 2)]))   # True


class Bar:
    def __init__(self, a):
        self.val = a

    def __eq__(self, other):
        return self.val == other.val


a1 = Bar(1)
a2 = Bar(1)
print(a1 == a2)
