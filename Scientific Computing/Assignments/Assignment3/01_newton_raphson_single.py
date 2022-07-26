from sympy import Symbol, diff, lambdify, sympify
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')


def derivative(expression):
    x = Symbol('x')
    f = lambdify(x, (func_ := sympify(expression)))
    f_prime = lambdify(x, (func_p_ := diff(expression)))

    print(f"The function is: {func_}")
    print(f"The derivative of the function is: {func_p_}")

    return f, f_prime


def newton_raphson(func, appx_root, err=0.01, max_iter=10, return_table=False):
    f, f_prime = derivative(func)

    root = None
    roots = []
    s: str = "\nn\t|x_n\t\t|f(x_n)\t\t|x_(n+1)\t|h\t\t\t|\n"
    for i in range(max_iter + 1):
        new_root = appx_root - (h := f(appx_root) / f_prime(appx_root))

        if abs(h) <= err:
            root = new_root
            s += f"{i}\t|{appx_root:0.5f}\t|{f(appx_root):0.5f}\t|{new_root:0.5f}\t|{h:0.5f}\t|\n"
            break
        else:
            s += f"{i}\t|{appx_root:0.5f}\t|{f(appx_root):0.5f}\t|{new_root:0.5f}\t|{h:0.5f}\t|\n"
            appx_root = new_root

        roots.append(new_root)

    # returns table
    if return_table:
        return root if root else "\nInsufficient Iteration!!!", roots, s

    return root if root else "\nInsufficient Iteration!!!", roots


if __name__ == '__main__':
    func: str = "x**3 - x**2 + 2"

    result = newton_raphson(func, 2.0, 0.01, 100, True)
    print(f"\nThe root is: {result[0]:0.6f}")

    table = result[-1]
    print(table)

    y = [(lambda x: x**3 - x**2 + 2)(i) for i in result[1]]

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot((x := np.linspace(-10, 10, 1000)), (lambda i: i**3 - i**2 + 2)(x), label="f(x)")
    plt.plot(result[1])
    plt.plot(result[1], y, '.', label="x")
    plt.axhline(0, color='red', alpha=0.2)
    plt.axvline(0, color='red', alpha=0.2)
    plt.xlabel("$x$")
    plt.ylabel("$x^3 - x^2 + 2$")
    plt.legend()
    plt.title('Newton-Raphson Single Variable')

    # second plot
    plt.subplot(2, 1, 2)
    plt.plot(result[1])
    plt.scatter(range(len(result[1])), result[1])
    plt.ylabel("$x$")

    plt.savefig('Newton_raphson_single.jpeg')
    plt.show()
