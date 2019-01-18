# Написать два алгоритма нахождения i-го по счёту простого числа.


def sieve(n):
    lst = [0] * n
    for i in range(n):
        lst[i] = i

    lst[1] = 0
    m = 2

    while m < n:
        if lst[m] != 0:
            j = m * 2
            while j < n:
                lst[j] = 0
                j = j + m
        m += 1

    prime_num = []

    for i in lst:
        if lst[i] != 0:
            prime_num.append(lst[i])

    print(prime_num)

    num = int(input('index = '))
    print(prime_num[num])

def sieve_2(n):
    lst_1 = []

    for num in range(2, n):
        if all(num % i != 0 for i in range(2, num)):
            lst_1.append(num)
    print(lst_1)

    num = int(input('index = '))
    print(prime_num[num])





