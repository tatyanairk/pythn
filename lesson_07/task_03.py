# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random

def gnome_sort(array):
    i = 1
    while i < len(array):
        if not i or array[i - 1] <= array[i]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

m = 5
n = 2 * m + 1

array = []

for i in range(n):
    i = random.randint(0, 100)
    array.append(i)

print(array)

new_array = gnome_sort(array)
print(new_array)
med_idx = len(new_array) // 2
mediana = new_array[med_idx]
print(f' Медиана =  {mediana}')