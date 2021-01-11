from random import random


def lnko(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def jacobi(a, n):
    if lnko(a, n) != 1: return 0
    assert (n > a > 0 and n % 2 == 1)
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0


def solovey_strassen(n, k=10):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    kitevo = (n - 1) / 2

    for i in range(k):
        a = int(random() * (n - 1)) + 1

        x = jacobi(a, n)

        y = (a ** kitevo) % n
        if y % n != x % n: return False

    return True


print(solovey_strassen(5, 5))
print(solovey_strassen(6, 5))
print(solovey_strassen(71483, 5))
print(solovey_strassen(2111309, 5))
