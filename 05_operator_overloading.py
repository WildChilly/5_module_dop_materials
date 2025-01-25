# -*- coding: utf-8 -*-

# Эмуляция операций и операторов python с помощью специальных методов

# Эмуляция операторов сравнения
#
# object.__eq__(self, other) - равенство двух объектов ==
# object.__ne__(self, other) - не равно !=
# object.__lt__(self, other) - строго меньше <
# object.__le__(self, other) - меньше или равно <=
# object.__gt__(self, other) - строго больше >
# object.__ge__(self, other) - больше или равно >=
#
# должны возвращать boolean - True/False
print('\n_____ 1')

class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __eq__(self, other):
        return self.content == other.content


my_backpack = Backpack(gift='бутерброд')
son_backpack = Backpack(gift='бутерброд')
son_backpack = Backpack(gift='Кокаин')

if my_backpack == son_backpack: # 1 вариант написания
    print('Как мы похожи...')
else:
    print('Не похожи совсем')

if Backpack.__eq__(self=my_backpack, other=son_backpack): # 2 вариант написания
    print('Как мы похожи...')

print('\n_____ 2')
# Эмуляция математических операций
# 2 + 2
# my_car + truck
#
# object.__add__(self, other) - сложение +
# object.__sub__(self, other) - вычитание -
# object.__mul__(self, other) - умножение *
# object.__truediv__(self, other) - деление /
# object.__floordiv__(self, other) - целочисленное деление //
# object.__mod__(self, other) - остаток от деления %
# object.__pow__(self, other) - возведение в степень **
# object.__lshift__(self, other) - побитовый сдвиг влево <<
# object.__rshift__(self, other) - побитовый сдвиг вправо >>
# object.__and__(self, other) - побитовое И &
# object.__xor__(self, other) - побитовое исключающее ИЛИ ^
# object.__or__(self, other) - побитовое ИЛИ |
#
# должны возвращать объект

class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __add__(self, other):  # Исправил не работающую часть кода строка 79
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        if isinstance(other, Backpack):  # добавляем содержимое другого рюкзака
            new_obj.content.extend(other.content)
        elif isinstance(other, list):  # добавляем список
            new_obj.content.extend(other)
        #new_obj.content.extend(other.content)
        return new_obj


my_backpack = Backpack(gift='бутерброд')
son_backpack = Backpack(gift='банан')
new_backpack = my_backpack + son_backpack
print(new_backpack)

other_backpack = my_backpack + ['яблоко', 'апельсин', 'кокаин']
print(other_backpack)

print('\n_____ 3')
# для операций расширенного присвоения служат методы. Каждый метод(все что написано слева от тире) в описании
# вызывается синтаксисом (символы все что написаны справа)
# object.__iadd__(self, other) - +=
# object.__isub__(self, other) - -=
# object.__imul__(self, other) - *=
# object.__itruediv__(self, other) - /+
# object.__ifloordiv__(self, other) - //=
# object.__imod__(self, other) - %=
# object.__ipow__(self, other) - **=
# object.__ilshift__(self, other) - <<=
# object.__irshift__(self, other) - >>=
# object.__iand__(self, other) - &=
# object.__ixor__(self, other) - ^=
# object.__ior__(self, other) - |=
#
# они изменяют сам объект (по месту, inplace)

class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __iadd__(self, other):
        self.content.extend(other.content)
        return self


my_backpack = Backpack(gift='бутерброд')
son_backpack = Backpack(gift='банан')
my_backpack += son_backpack
print(my_backpack)


# Не обязательно возвращать объект такого же класса(типа)
class Bread:

    def __str__(self):
        return 'Я хлеб'

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sausage:

    def __str__(self):
        return 'Я колбаса'

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sandwich:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я бутерброд. Состою из ' + str(self.part1) + ' и ' + str(self.part2)


borodinsky = Bread()
salami = Sausage()
result = borodinsky + salami
print(result)


# эмуляция вызова функции - это когда объект ведет себя как функция
# object.__call__(self[, args...]) - вызов как функции
print('\n_____ 4')
def func(*args, **kwargs):
    print(args, kwargs)


print(func)
func(a=2, b=2)


class MyFunction:

    def __call__(self, *args, **kwargs):
        print(args, kwargs)


func = MyFunction()
print(func)

func(a=2, b=2)

print('\n_____ 5')
# это используется для немного странных и увлекательных вещей :)
# погрузимся чуть-чуть в функциональный стиль
class Multyplier:

    def __init__(self, factor=2):
        self.factor = factor

    def __call__(self, *args):
        res = []
        for item in args:
            res.append(item * self.factor)
        return res


mul_by_27 = Multyplier(factor=25)
result = mul_by_27(1, 2, 3, 4)
print(result)

multipiers = []
for factor in (2, 3, 4, 5):
    mul = Multyplier(factor=factor)
    multipiers.append(mul)
print(multipiers)

for mul in multipiers:
    print(mul(10, 20, 30))
# В результате, этот код создает несколько экземпляров
# класса Multyplier с разными факторами умножения и использует
# их для умножения списков чисел на эти факторы.

# все специальные методы перечислены в
#   https://docs.python.org/3/reference/datamodel.html#special-method-names
