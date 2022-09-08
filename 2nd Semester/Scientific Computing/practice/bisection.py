import numpy as np


def bisection(func, a, b, e):
    if func(a) * func(b) >= 0:
        return None

    while abs(b - a) >= e:
        root = (a + b) / 2.0

        if func(root) == 0:
            return root
        elif func(a) * func(root) < 0:
            b = root
        else:
            a = root

    return root


if __name__ == '__main__':
    def f(x):
        return np.power(x, 4) - 5 * x + 1


    a_val = 0.0
    b_val = 1.0
    tolerance_level = 0.01

    root = bisection(f, a_val, b_val, tolerance_level)

    print(root)
