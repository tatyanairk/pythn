# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

import sys

n = int(input('Введите любое натуральное число: '))
s = 0

for i in range(1, n+1):
    s += i

p = n * (n + 1) // 2

# if s == p:
#    print('{} = {}. Равенство выполнилось!'.format(s, p))

# else:
#    print('{} != {}. Равенство не выполнилось :('.format(s, p))

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

el = [n, s, i, p]
analyze(el)

# type = <class 'list'>, size = 96, object = [35, 630, 35, 630]
#	 type = <class 'int'>, size = 28, object = 35
#	 type = <class 'int'>, size = 28, object = 630
#	 type = <class 'int'>, size = 28, object = 35
#	 type = <class 'int'>, size = 28, object = 630