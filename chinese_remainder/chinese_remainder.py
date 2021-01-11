# coding=utf-8
import functools


# Euclidean extended algorithm
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        d, x, y = extended_euclidean(b % a, a)
        return d, y - (b // a) * x, x


def chinese_remainder(a, n):
    modulus = functools.reduce(lambda x, y: x * y, n)
    multipliers = []
    for n_i in n:
        N = modulus / n_i
        gcd, inverse, y = extended_euclidean(N, n_i)
        multipliers.append(inverse * N % modulus)

    result = 0
    for multi, a_i in zip(multipliers, a):
        result += multi * a_i
    return result % modulus


n = [7, 6, 5]
a = [6, 2, 0]

for i in range(3):
    print("x ≅ " + str(a[i]) + " mod " + str(n[i]))
print("x = " + str(chinese_remainder(a, n)))