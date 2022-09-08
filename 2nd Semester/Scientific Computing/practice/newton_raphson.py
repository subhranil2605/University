import numpy as np


def newton_raphson(func, func_1, appx, err, m_iter):
    for _ in range(m_iter):
        h = func(appx) / func_1(appx)
        new_root = appx - h

        if abs(h) >= err:
            appx = new_root
        else:
            return new_root


def f(x):
    return x ** 3 - x ** 2 + 2


def f_1(x):
    return 3 * x ** 2 - 2 * x


if __name__ == '__main__':
    result = newton_raphson(f, f_1, 2.0, 0.01, 20)
    print(result)
