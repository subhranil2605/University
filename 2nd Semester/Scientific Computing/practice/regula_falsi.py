def regula_falsi(func, a, b, err, m_iter):
    if func(a) * func(b) >= 0:
        return None

    for _ in range(m_iter):
        root = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if func(root) >= err:
            if func(root) == 0:
                return root
            elif func(a) * func(root) < 0:
                b = root
            elif func(root) * func(b) < 0:
                a = root
        else:
            break

    return root


if __name__ == '__main__':
    def func(x):
        return x ** 3 - x ** 2 + 2


    result = regula_falsi(func, -2.0, 0.0, 0.001, 6)
    print(result)
