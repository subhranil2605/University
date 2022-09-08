import numpy as np


def secant(func, a, b, e=0.001):
    while abs(b - a) >= e:
        root = (a * func(b) - b * func(a)) / (func(b) - func(a))
        a = b
        b = root
    return root


if __name__ == '__main__':
    def f(x):
        return x * np.exp(x) - 1


    a = 0.0
    b = 1.0

    result = secant(f, a, b)

    print(result)
