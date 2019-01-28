# По введенным пользователем координатам двух точек вывести уравнение прямой,
# проходящей через эти точки.

import sys

print("Введите целые координаты двух точек")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

k = (y2 - y1) / (x2 - x1)
b = y2 - (((y2 -y1) / (x2 - x1)) * x2)

#print("y = {}x + {}".format(k, b))

def analyze(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                analyze(key, level + 1)
                analyze(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                analyze(item, level + 1)

el = [x1, x2, y1, y2, k, b]
analyze(el)

# type = <class 'list'>, size = 112, object = [4, 5, 6, 3, -3.0, 18.0]
#	 type = <class 'int'>, size = 28, object = 4
#	 type = <class 'int'>, size = 28, object = 5
#	 type = <class 'int'>, size = 28, object = 6
#	 type = <class 'int'>, size = 28, object = 3
#	 type = <class 'float'>, size = 24, object = -3.0
#	 type = <class 'float'>, size = 24, object = 18.0

# 64-х раздрядная операционная система, версия Python 3.7.1