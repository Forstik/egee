#int - целочисленный тип данных
from operator import truediv

a = ""

#str - строчный тип данных

s = [1,2,"a", [1,2,3,4]]
#list - список элементов не связанных по типу элементов

a = 0.5
print(type(a))
#type - выводит тип данных объекта
#float дробный тип данных

#bool - 0/1 false/true
# a = false

# s ={"key": "value","key2": "value"}
# # dict - словарь(набор элементов + значение)
# print(type(s))

# s ={1,2,3,4,5,6,65,6,6,56,5,65,65,6}
# print(type(s),s)
#set - набор уникальных элементов

# a = 1.3

s = (1,2,3,4,5,6,7,8,13123)
#tuple - Набор  неизменяемых элементов

# s = 10/5
# print(s)

# float > int
# s = 10 + 2.0
# print(s)

# float > int > bool
# a = True
# b = 5
# result = a + b
# print(result)

# s = int(value)

# print(int(10.8)) ok
# print(int("10")) ok
# prit(int("10.3"))) ne ok

# print(float("10.3"))

# a = int(float("10.2"))
# print(a)
a = str([False])
print(a , type(a))

# a = list("hello")
# a = list((1,2,3,4))
# a = list(10)
# print(a)
# tuple()
# dict()

# input() print()

# g =(list("Python"))
# print(g)

# int_a = int(input())
# float_a = float(input())
# str_a = input()
#
# print(int_a, float_a, str_a, sep=', ')
#
# nums = [1,2,3,4,5]
# print(set(nums))

# product = {"название": "ноутбук",
#            "цена" : 55000,
#            "в наличии" : True}
# print(product["название"], ["цена"], product["в наличии"])
#
# # Даны кортеж coords = (55, 75, 10) и
# # список labels = ["широта", "долгота", "высота"].
# # Выведите на экран первое значение кортежа с
# # первой подписью из списка, а затем второе
# # значение кортежа со второй подписью,
# # используя индексацию по номеру элемента,
# # через разделитель "; ".
#
# coords = (55, 75, 10)
# labels = ["широта", "долгота", "высота"]
# print(coords[0], labels[0], coords[1], labels[1], sep=";")

# #+- * / ** % //
# print("hello" + "world") #конкатенация
# print(set([1,2,3] + [3,4,5])
# print((1,2,3) + (3,4,5)
# # print([1,2,3] - [3,4,5])
# print(abs(-10) % 3 )

print(2 ** (1/2))
#() - 1
#** - 2
#* / // % - 3
#+ - - 4