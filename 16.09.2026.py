# from random import randrange
# a = randrange(1, 99,2) # 1 3 5 7 9 11 вот почему степ 2
# print(a)

# from math import *
# from random import *
# a = randint(0, 1000000)
# b = randint(0, 1000000)
#
# k = log10(a)
# l = b / 3
# M = k - l
# print(log2(M))

# from random import randint
# from math import ceil
# num = 21
# num1 = num / 7
# num2 =ceil(num1)
# print(num2)

# from random import *
# from math import sqrt, floor
# a = random()
# b = a * 10000
# c = sqrt(b)
# print(floor(c),int(c), c // 1)

#Задания 7 (Работа с изображением)
# 1 - N = 2 в степени i
#N - количество цветов в палитре
# i -глубина цвета
#формула хартли

# from math import ceil
# S = 2560*5040
# B = 14175 * 2 ** 13
# i = ceil(B / S)
# N = 2 ** i
# 2.1

# from math import ceil
S = 7680 * 4320
B = 4010
N = 2 ** 16
D = 9 * 2 ** 33
i = 16 #глубина цвета
L = S * i #вес одного изображения
H = D / L
amount = int(H)
print(4010 - int(B / H) * amount)
