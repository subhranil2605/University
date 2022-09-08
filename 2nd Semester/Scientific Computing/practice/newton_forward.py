import numpy as np
import math

x = np.arange(0.1, 0.6, 0.1)
y = np.exp(2 * x)

# finite difference
h = x[1] - x[0]


# create table for the calculation
def get_table(y):
    size = len(y)
    coef = np.zeros((size, size))

    # set the first column of the coef matrix to be y
    coef[:, 0] = y

    for i in range(1, size):
        for j in range(size - i):
            coef[j][i] = coef[j + 1][i - 1] - coef[j][i - 1]

    print(coef)
    return coef


# getting the table
tabl = get_table(y)


# formula implementation
def newton_forward(x_value, table, x, y):
    result = y[0]
    for i in range(1, len(x)):
        rk = 1
        an = table[0][i] / (math.factorial(i) * np.power(h, (i)))
        for j in range(i):
            rk *= x_value - x[j]

        result += rk * an

    return result


x_val = 0.05
result = newton_forward(x_val, tabl, x, y)

print(f"Value of f({x_val}) = {result:0.6f}")
