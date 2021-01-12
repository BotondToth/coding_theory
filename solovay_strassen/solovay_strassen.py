from random import random
from jacobi import Jacobi


def lnko(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def solovey_strassen(n, k=10):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    exp = (n - 1) / 2

    for i in range(k):
        a = int(random() * (n - 1)) + 1

        x = Jacobi(a, n).calculate() % n

        y = pow(a, exp) % n
        if x != y:
            return False

    return True


def solovey_strassen_slow(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    exp = (n - 1) / 2

    A = []
    for i in range(1, n-1):
        if lnko(i, n) == 1:
            A.append(i)

    for a in A:
        x = Jacobi(a, n).calculate() % n

        y = pow(a, exp) % n
        if x != y:
            return False

    return True


print(solovey_strassen(5, 5))
print(solovey_strassen(6, 5))
print(solovey_strassen(71483, 5))
print(solovey_strassen(2111309, 5))

""" --------------------------------- """

#print(solovey_strassen_slow(5))
#print(solovey_strassen_slow(6))
#print(solovey_strassen_slow(71483))

""" --------------------------------- """
