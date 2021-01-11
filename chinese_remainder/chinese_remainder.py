# coding=utf-8
import functools


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - b / a * x1
    y = x1
    return gcd, x, y


def chinese_remainder(a, n):
    modulus = functools.reduce(lambda x, y: x * y, n)
    sum = 0

    for n_i, a_i in zip(n, a):
        N = modulus / n_i
        gcd, u_i, y = extended_gcd(N, n_i)
        sum += (u_i * N % modulus) * a_i

    print(str(sum) + " ≅ x mod " + str(modulus))

    return sum % modulus


n = [5, 6, 7]
a = [3, 2, 4]

for i in range(3):
    print("x ≅ " + str(a[i]) + " mod " + str(n[i]))
print("x = " + str(chinese_remainder(a, n)))
