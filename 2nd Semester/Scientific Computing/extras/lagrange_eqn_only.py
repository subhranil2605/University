import numpy as np
from numpy import ndarray
from tabulate import tabulate
from sympy import symbols, expand, lambdify, latex
import matplotlib.pyplot as plt



def func(x: int | float) -> float:
    """Returns the value of the given function"""
    
    return 1 / (1 + np.power(x, 2))


# creating a symbol
x = symbols('x')


def lagrange_func(x_values: ndarray, y_values: ndarray) -> list:
    
    assert len(x_values) == len(y_values), "Length of the two lists should be same!!!"

    # to store the expressions
    expressions = []
    
    for i, y_val in enumerate(y_values):
        l_i_expr = y_val
        for j in range(len(x_values)):
            if j != i:
                l_i_expr *= (x - x_values[j]) / (x_values[i] - x_values[j]) # expression
                
        expressions.append(l_i_expr)

    return expressions


if __name__ == "__main__":
    x_vals: ndarray = np.linspace(-5, 5, 11)
    y_vals: ndarray = func(x_vals)


    # for tabulating the values
    table: list[list] = [[i, j] for i, j in zip(x_vals, y_vals)]

    # result
    equation = lagrange_func(x_vals, y_vals)
    print(equation)

    # expand the sum of the equations
    equation = expand(sum(equation))

    # tabulating the table
    print(tabulate(table, headers=["X", "Y"], showindex="always", tablefmt="pretty"))

    print(f"\nThe equation is {equation}")


    # __________________________________________________________________________________
    # plottig
    
    offset = 0         # offset for plotting the x range

    # x values
    x_s = np.linspace(x_vals[0] - offset, x_vals[-1] + offset, 100)

    # calculated y values
    y_s = [equation.subs(x, i) for i in x_s]

    plt.scatter(x_vals, y_vals, c='k', label="Given Points")    # Given points scatter plot
    plt.plot(x_s, y_s, label="$p_{10}$")     # line plot 

    plt.title(f"Lagrange Interpolation")
    plt.ylabel(r"$f(x) = \frac{1}{1+x^2}$")
    plt.xlabel("$x$")
    
    # actual function 
    plt.plot(x_s, func(x_s), label="$f(x)$")
    
    plt.legend()
    plt.show()

    
