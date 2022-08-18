"""
Lagrange Interpolation
Subhranil Sarkar

packages used:
    tabulate:
    pip install tabulate

    sympy:
    pip install sympy
"""

from tabulate import tabulate
from sympy import symbols, expand, lambdify, latex
import matplotlib.pyplot as plt
import numpy as np


x = symbols('x')
plt.style.use('seaborn-whitegrid')


def lagrange_func(x_values: list, y_values: list, val):
    """
    Lagrange Interpolation

    :param x_values: list of the given data points
    :param y_values: list of the other data points
    :param val: value given
    :raises AssertionError: if the length of the two lists do not match
    :retuns: calculated value for x
    """
    
    assert len(x_values) == len(y_values), "Length of the two lists should be same!!!"

    # to store the result 
    result = 0

    # to store the expressions
    expressions = []
    
    for i, y_val in enumerate(y_values):
        l_i = y_val
        l_i_expr = y_val
        for j in range(len(x_values)):
            if j != i:
                l_i_expr *= (x - x_values[j]) / (x_values[i] - x_values[j])
                l_i *= (val - x_values[j]) / (x_values[i] - x_values[j])  # formula
                
        result += l_i
        expressions.append(l_i_expr)

    return result, expressions


if __name__ == "__main__":
    x_vals: list = [300, 304, 305, 307]
    y_vals: list = [2.4771, 2.4829, 2.4843, 2.4871]
    
    val: int = 301

    # for tabulating the values
    table: list[list] = [[i, j] for i, j in zip(x_vals, y_vals)]

    # result
    rslt, equation = lagrange_func(x_vals, y_vals, val)

    # expand the sum of the equations
    equation = expand(sum(equation))

    # tabulating the table
    print(tabulate(table, headers=["X", "Y"], showindex="always", tablefmt="pretty"))
    
    print(f"For X: {val} the value of Y: {rslt:0.6f}")
    
    print(f"\nThe equation is {equation}")


    # __________________________________________________________________________________
    # plottig
    
    offset = 10         # offset for plotting the x range

    # x values
    x_s = np.linspace(x_vals[0] - offset, x_vals[-1] + offset, 100)

    # calculated y values
    y_s = [equation.subs(x, i) for i in x_s]

    plt.figure(figsize=(12, 8))
    plt.scatter(x_vals, y_vals, c='k', label="Given Points")    # Given points scatter plot
    plt.scatter(val, rslt, marker='d', c='red', label=f"Calculate Point for $x={val}$") # calculated point
    plt.plot(x_s, y_s, label="Calculated polynomial graph")     # line plot 

    plt.title(f"Lagrange Interpolation\n${latex(equation)}$")
    plt.ylabel("$f(x)$")
    plt.xlabel("$x$")
    
    plt.legend()
    plt.savefig("lagrange.jpg", dpi=300)
    plt.show()

    
    
    
