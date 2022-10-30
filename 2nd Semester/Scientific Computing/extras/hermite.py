"""
Subhranil Sarkar
github.com/subhranil2605

modules need to be installed 
  pip install tqdm
  pip install sympy
  pip install numpy
  pip install matplotlib
"""



import numpy as np
from numpy import ndarray
from sympy import symbols, expand
import matplotlib.pyplot as plt
from tqdm import tqdm


def func(x):
    """Given function"""
    return 1 / (1 + np.power(x, 2))


def func_p(x):
    """Derivative of the function"""
    return - 2 * x / np.power(1 + np.power(x, 2), 2)

# for creating polynomial
x = symbols('x')


def lagrange_func(x_values: ndarray, y_values: ndarray):
    
    assert len(x_values) == len(y_values), "Length of the two lists should be same!!!"

    # to store the expressions
    expressions = []
    
    for i, y_val in enumerate(y_values):
        l_i_expr = y_val
        for j in range(len(x_values)):
            if j != i:
                l_i_expr *= (x - x_values[j]) / (x_values[i] - x_values[j]) # expression
                
        expressions.append(l_i_expr)

    return expand(sum(expressions))


def hermite(xs):
    """divide difference table generation"""

    n = len(xs)
    q = np.zeros((2 * n, 2 * n))
    z = np.zeros(2 * n)

    for i in range(n):
        z[2 * i] = xs[i]
        z[2 * i + 1] = xs[i]
        q[2 * i][0] = func(xs[i])
        q[2 * i + 1][0] = func(xs[i])
        q[2 * i + 1][1] = func_p(xs[i])

        if i != 0:
            q[2 * i][1] = (q[2 * i][0] - q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])

    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            q[i][j] = (q[i][j - 1] - q[i - 1][j - 1]) / (z[i] - z[i - j])

    return q, z


def hermite_poly_generation(coeffs, z):
    """Hermite Polynomial generation"""

    expressions = []
    for i in range(len(z)):
        expr = coeffs[i]
        for j in range(i):
            expr *= x - z[j]
        expressions.append(expr)

    return expand(sum(expressions))


if __name__ == "__main__":
    x_s = np.linspace(-5, 5, 11)
    table, z = hermite(x_s)
    coeffs = table.diagonal()

    lagrange_poly = lagrange_func(x_s, func(x_s))
    hermite_poly = hermite_poly_generation(coeffs, z)

    # plot
    xs = np.linspace(-5, 5, 500)
    l_values = [lagrange_poly.subs(x, i) for i in tqdm(xs)]
    h_values = [hermite_poly.subs(x, i) for i in tqdm(xs)]

    plt.plot(xs, func(xs), label=f"Actual")
    plt.plot(xs, l_values, label=f"Lagrange")
    plt.plot(xs, h_values, label=f"Hermite")

    plt.legend()
    plt.show()
