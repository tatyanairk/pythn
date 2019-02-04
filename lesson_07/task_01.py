# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array [i + 1] = array [i + 1], array[i]
        n += 1

array = []

for i in range(10):
    i = random.randint(-100, 100 - 1)
    array.append(i)

print(array)

bubble_sort(array)
print(array)
