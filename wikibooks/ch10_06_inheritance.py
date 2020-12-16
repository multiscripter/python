class Papa:
    def say(self):
        return 'I am papa'


class StupidSon(Papa):
    pass


class OrdinarySon(Papa):
    def say(self):
        return 'I am son'


class SmartSon(Papa):
    def say(self):
        p = super(SmartSon, self).say()
        return 'I am son. My Papa said: ' + p


dad = Papa()
stipudSon = StupidSon()
ordinarySon = OrdinarySon()
smartSon = SmartSon()

print(dad.say())  # I am papa
print(stipudSon.say())  # I am papa
print(ordinarySon.say())  # I am son
print(smartSon.say())  # I am son. My Papa said: I am papa


# Множественное наследование.
# Для выбора реализации Python использует метод MRO (Method Resolution Order).
# То есть берёт первую реализацию из списка.

# Глупый пример "Проблемы ромба".
class Device:
    def work(self):
        pass


class Printer(Device):
    def work(self):
        return 'I am printing.'


class Scanner(Device):
    def work(self):
        return 'I am scanning.'


class MFD(Printer, Scanner):
    pass


mfd = MFD()
print(mfd.work())  # I am printing.


# Метод __init__()
class Animal:
    def __init__(self):
        self.name = 'Animal'


class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super(Cat, self).__init__()


cat = Cat('Red')
print(cat.name)  # Animal


# Композиция.
class MFD2:
    def __init__(self):
        self.printer = Printer()
        self.scanner = Scanner()

    def work(self):
        return self.scanner.work() + ' ' + self.printer.work()


mf2 = MFD2()
print(mf2.work())

# Перегрузка методов. Не работает !!!!!!!
# class Overload:
#	def print(self, arg):
#		print(f'arg: {arg}')
#
#	def print(self, arg1, arg2):
#		print(f'arg1: {arg1}, arg2: {arg2}')
#
# over = Overload()
# over.print('First') # TypeError: print() missing 1 required positional argument: 'arg2'
# over.print('First', 'second')
