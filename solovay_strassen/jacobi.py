class NotOddException(Exception):
    def __init__(self, x):
        print(str(x) + " nem paratlan!")


class NotPositiveException(Exception):
    def __init__(self, x):
        print(str(x) + " nem pozitiv!")


def lnko(x, y):
    while y != 0:
        t = y
        y = x % y
        x = t
    return x


class Jacobi:

    def __init__(self, a, p):
        if p < 0:
            raise NotPositiveException(p)

        if p % 2 == 0:
            raise NotOddException(p)

        self.a = a
        self.p = p
        if lnko(a, p) != 1:
            self.coPrime = False
        else:
            self.coPrime = True

    @staticmethod
    def __5_case__(p):
        exp = (pow(p, 2) - 1) // 8
        return pow(-1, exp)

    @staticmethod
    def __6_case__(x, y):
        # kvadratikus reciprocitas
        if x % 4 == 1 or y % 4 == 1:
            return 1

        return -1

    def calculate(self):
        if not self.coPrime:
            return 0
        if self.a == -1:
            return pow(-1, (self.p - 1) // 2)
        if self.a == 1:
            return 1
        if self.a == 2:
            return self.__5_case__(self.p)
        if self.a % 2 == 0:
            # szamlaloban multiplikativ
            return Jacobi(self.a // 2, self.p).calculate() * Jacobi(2, self.p).calculate()

        return Jacobi(self.p % self.a, self.a).calculate() * self.__6_case__(self.a, self.p)
