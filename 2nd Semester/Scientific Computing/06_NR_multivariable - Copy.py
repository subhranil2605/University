import numpy as np
from sympy import symbols, lambdify, sympify, diff

def part_diff(expression):
    x, y = symbols('x y')
    return lambdify([x, y], sympify(expression)), lambdify([x, y], diff(expression, x)), lambdify([x, y], diff(expression, y))

def newton_raphson_two(func_1, func_2, x_k, y_k, max_iter):
    f, f_x, f_y = part_diff(func_1)
    g, g_x, g_y = part_diff(func_2)
    result = np.zeros((2, 1))
    for _ in range(max_iter):      
        X_k_1 = np.array([[x_k], [y_k]]) - np.dot(((1 / (f_x(x_k, y_k) * g_y(x_k, y_k) - g_x(x_k, y_k) * f_y(x_k, y_k))) * np.array([[g_y(x_k, y_k), -f_y(x_k, y_k)],[-g_x(x_k, y_k), f_x(x_k, y_k)]])), np.array([[f(x_k, y_k)], [g(x_k, y_k)]]))
        x_k, y_k = X_k_1[0, 0], X_k_1[1, 0]
        result = X_k_1
    return result

def main():
    func_1,func_2 = "x**2 + x*y + y*y - 7", "x**3 + y**3 - 9"
    initial_1, initial_2 = 1.5, 0.5
    max_iteration = 3
    r = newton_raphson_two(func_1, func_2, initial_1, initial_2, max_iteration)
    print(f"Approximate value of x: {round(r[0, 0], 4)}\nApproximate value of y: {round(r[1, 0], 4)}")


if __name__ == '__main__':
    main()
