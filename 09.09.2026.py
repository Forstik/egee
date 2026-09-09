# a = 0.1 + 0.2
# print(a)
from random import random

# print(round(0.1 + 0.2 == 0.3))

#in - оператор принадлежности
# print("World" in "Hello World")#str
# print(6 in [1,2,3,4,5,5]) #list
# a = {"key": "value", "key1" : "value1"} #dict
# print("key" in a) #ищем по ключу

# srt tuple
# print(6 in {1,2,4,5,6}) #итерируемые объекты
# print(6 in (1,2,3,4,5,6))

# print(not in) #не входит

# is / is not

# a = 10 ** 10
# b = a
# print(a is b)
# print(id(a), id(b))
# jhjhj = [1,2,3]
# g = [1,2,3]
# print(id(a), id(b))
# print(a is b,a == b)
#id проверка на индентичность

# a = 5
# b = 5.0
# print(a == b)

# a = 3
# b = 8
# print(a < b)

# a = [1,2,3]
# b = a
# print(a is b)

# += - a+b

# numbers = [10,20,30,40]
# print(25 in numbers)
#
# numbers = [10,20,30,40]
# print(40 not in numbers)

# x = True
# y = False
# print(x or y)

# a = int(input())
# b = int(input())
# print(a,b)
# print(a == b)
# a += 10
# print(a > b)

# + - / ** **1/2 % * //

# import math #вариант 1
# result = math. sqrt(16)  #sqrt - означет корень
# math.
# print(result)

# from math import sqrt, log2
# print(sqrt(16))
from math import *

from math import (sqrt, ceil, floor, pi, log2, log10, log)

# print(sqrt()) #корень от числа квадратного
# print(ceil(7.1)) #округлениие в большую сторону
# print(floor (9.6))#окргуление в меньшию сторону
# print(pi)
# print(log2(10), log10(100), log(128,sqrt(2)))

# import math
# math.radians(90)
# print(math.degrees(math.pi))

# from random import random, uniform, randint,randrange

#работа с числом
# print(random()) #число от 0 до 1
# print(uniform(2.5, 5.5)) #число от a до b дробное
# print(randint(2,10)) #число от a до b целое
# print(randrange(0, 20, 2)) # выбрать случайное четное число от 0 до 20

#работать с последовательностями
from random import choices, sample, shuffle
# fruits = ["киви","банан", "вишню"]
#fruits = choices(fruits)
# result = choices(fruits, k = 2)
# print(result)

# nums = [1,2,3,4,5,6,7,8]
# result = sample(nums,3) # k- сколько чиссел выдает случайно
# print(result)
# shuffle(nums) # shuffle - меняет порядок делает хаотичным
# print(nums)

#2A
# print(int("num",base)) # перевод num из системы base

# s = bin(20) #перевод из десятичной в двоичною систему счисления, смотреть после b
# print(s)

# s = oct(20) # перевод из 10й в 2ю систему
# s = bin(20) [2:]

# s = format (20, "b") #о - восьмиричная, b - двоичная, x - 16
# print(f"{20:b}")

# s = hex(20) #16 система
