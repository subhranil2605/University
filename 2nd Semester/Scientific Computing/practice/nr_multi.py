import numpy as np


def newton_raphson_two(f, f_x, f_y, g, g_x, g_y, x_k, y_k, m_iter):
    for _ in range(m_iter):
        X_k = np.array([
            [x_k],
            [y_k]
        ])

        F = np.array([
            [f(x_k, y_k)],
            [g(x_k, y_k)]
        ])

        J_k = np.array([
            [f_x(x_k, y_k), f_y(x_k, y_k)],
            [g_x(x_k, y_k), g_y(x_k, y_k)]
        ])

        J_k_inv = np.linalg.inv(J_k)

        X_k_next = X_k - np.dot(J_k_inv, F)

        x_k, y_k = X_k_next[0, 0], X_k_next[1, 0]

    return X_k_next


if __name__ == '__main__':
    def f(x, y):
        return x ** 2 + x * y + y ** 2 - 7


    def g(x, y):
        return x ** 3 + y ** 3 - 9


    def f_x(x, y):
        return 2 * x + y


    def f_y(x, y):
        return x + 2 * y


    def g_x(x, y):
        return 3 * x ** 2


    def g_y(x, y):
        return 3 * y ** 2


    result = newton_raphson_two(f, f_x, f_y, g, g_x, g_y, 1.5, .5, 3)

    print(result)
