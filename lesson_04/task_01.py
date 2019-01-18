# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# python -m timeit -n 100 -s "import task_01" "task_01.max_min(10)"
# python -m timeit -n 100 -s "import task_01" "task_01.max_min_2(20)"

import random
import cProfile

# 1-й вариант

def max_min(size):
    array = [random.randint(1, 100) for _ in range(size)]
    mn = 0
    mx = 0

    for i in range(size):
        if array[i] < array[mn]:
            mn = i
        elif array[i] > array[mx]:
            mx = i

    b = array[mn]
    array[mn] = array[mx]
    array[mx] = b

# 100 loops, best of 5: 19.9 usec per loop - 10
# 100 loops, best of 5: 28.7 usec per loop - 15
# 100 loops, best of 5: 39.1 usec per loop - 20
# 100 loops, best of 5: 187 usec per loop - 100

# cProfile.run('max_min(20)')

# 1    0.000    0.000    0.000    0.000 task_01.py:7(max_min) - 10
# 1    0.000    0.000    0.000    0.000 task_01.py:7(max_min) - 15
# 1    0.000    0.000    0.000    0.000 task_01.py:7(max_min) - 20

# 2-й вариант

def max_min_2(size):
    array = [random.randint(1, 100) for _ in range(size)]
    mn = 0
    mx = 0

    mn = min(array)
    mx = max(array)
    imn = array.index(mn)
    imx = array.index(mx)
    array[imn], array[imx] = array[imx], array[imn]

# 100 loops, best of 5: 19.5 usec per loop - 10
# 100 loops, best of 5: 29 usec per loop - 15
# 100 loops, best of 5: 37.2 usec per loop - 20
# 100 loops, best of 5: 174 usec per loop - 100

# cProfile.run('max_min_2(20)')

# 1    0.000    0.000    0.000    0.000 task_01.py:37(max_min_2)
# 1    0.000    0.000    0.000    0.000 task_01.py:37(max_min_2)
# 1    0.000    0.000    0.000    0.000 task_01.py:37(max_min_2)

# При трех замерах с шагом 5, время выполнения двух алгоритмов не показало существенных отличий.
# При увеличении n до 100, первый алгоритм показал большее время выполнения, чем второй алгоритм.
