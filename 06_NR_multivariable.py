import numpy as np
from sympy import symbols, lambdify, sympify, diff


def part_diff(expression):
    # creating the sympy symbols
    x, y = symbols('x y')

    # creating the python function objects from the sympy expression

    # actual function
    f = lambdify([x, y], sympify(expression))

    # partial diff w.r.t "x"
    f_x = lambdify([x, y], diff(expression, x))

    # partial diff w.r.t "y"
    f_y = lambdify([x, y], diff(expression, y))

    # returning the tuple of python function objects
    return f, f_x, f_y


def newton_raphson_two(func_1, func_2, x_k, y_k, max_iter):

    # getting the function objects from the derivative function 
    f, f_x, f_y = part_diff(func_1)
    g, g_x, g_y = part_diff(func_2)

    # creating the result matrix 2x1 using 0 values
    result = np.zeros((2, 1))
    
    for i in range(max_iter):
        # matrix of x_k and y_k
        X_k = np.array([x_k, y_k])[:, np.newaxis]   

        # matrix of the functions at point (x_k, y_k)
        F = np.array([f(x_k, y_k), g(x_k, y_k)])[:, np.newaxis]    

        # calculating the value of D_k
        D_k = f_x(x_k, y_k) * g_y(x_k, y_k) - g_x(x_k, y_k) * f_y(x_k, y_k)     
        
        # Jacobian inverse
        J_k_inv = (1 / D_k) * np.array([
            [g_y(x_k, y_k), -f_y(x_k, y_k)],
            [-g_x(x_k, y_k), f_x(x_k, y_k)]
        ])
        # calculating the roots using the NR method
        X_k_1 = X_k - np.dot(J_k_inv, F)

        # updating the values of x_k and y_k for the next iteration
        x_k, y_k = X_k_1[0, 0], X_k_1[1, 0]

        # stroing the root matrix in the result variable
        result = X_k_1

    # returing the root matrix 
    return result


def main():
    func_1 = "x**2 + x*y + y*y - 7"
    func_2= "x**3 + y**3 - 9"

    initial_1, initial_2 = 1.5, 0.5
    max_iteration = 3

    r = newton_raphson_two(func_1, func_2, initial_1, initial_2, max_iteration)

    print(f"Approximate value of x: {round(r[0, 0], 4)}")
    print(f"Approximate value of y: {round(r[1, 0], 4)}")


if __name__ == '__main__':
    main()
