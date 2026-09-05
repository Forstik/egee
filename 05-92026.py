# s = 2 / 3 - неявное
# s = int("10.2")

# * / + - // **  1/2 %
# a = input()
# b = input()
# c = input()
# print(a + b)

# 3)numbers = [1,2,3,2,1]
# print(set(numbers))
# # print(type(s),s)
#
# 2)a = input()
# b = input()
# print(int(a) + int(b))

# 1) a = int(input())
# b = int(input())
# c = int(input())
# print(a+b, b-c, sep = ";")

# round() - модуль для округления числа
# round(num, count)
# num - число
# count - кол-во цифр после запятой
# a = round(4.51623742349,2)
# print(a)

# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a + b + c) /2
# area = (p * (p -a) * (p - b) * (p -c)) ** 0.5
# print(round(area,2))

# num = int(input())
# one = num % 10
# two = num % 100 // 10
# three = num % 1000 // 100
# four = num // 1000 % 10
# five = num // 10000
# print(one + two + three + four + five)

# print (True == False,True != False, 4 >= 1, 1 <= 10, 9 >20,  9 < 20 )
# print((True == True) == (False == False))

# print(True and False)

# and or not
# and - логическое и

# a b (a and b)
# 1 1 True
# 0 1 False
# 1 0 False
# 0 0 True

# a b (a or b)
# 1 1 True
# 0 1 True
# 1 0 True
# 0 0 False

# a (not a)
#  True False
# False True

# a = bool(0.1)
# s = [0]
# a = bool(s)
# print(a)

# s = {}
# print(bool(set(s)))
# print(bool(s))

x = False
y = False
print(x or y)

x = True
y = False
print(x == y)

x = True
y = True
print(not(x and y))

x = False
y = True
z = False
print(x and y) or z

x = False
y = False
z = True
print(x == y) or not z

# Вычислите значение логического выражения: (x↓y)∨¬z, если x = ложь, y = истина, z = истина.

x = False
y = True
z = True
print(y and x) or not z

# Стрелка Пирса ↓
# Отрицание дизъюнкции
# a b a↓b
# 0 0 1
# 1 0 0
# 0 1 0
# 1 1 0

#Импликация стрелка вправо
# Из истины нельзя получить ложь
# a b a стрелка вправо b
# 0 0 True
# 0 1 True
# 1 0 False
# 1 1 True
a = False
b = True
print(a <= b)

#Исключающие или знак прицела
# Возвращает истину только тогда когда 1 из аргументов истина а другой ложь
# a b = a знак прицела b
# 0 0 0
# 1 0 1
# 0 1 1
# 1 1 0

# a = False
# b = True
# print(a стрелкак вверх b)

#Штрих Шеффера |
#Отрицание коньюкции
# a b a|b
# 0 0 1
# 0 1 0
# 1 0 1
# 1 1 0

# 1 - ()
# все мат операции
# 2 - not
# 3 - and
# 4 - or
# 5 - стрелка вправо и значек прицела
# 6 - ==

print(1 + 5 == 5 + 20)
# если не уверен в том что делаешь ставть скобки




