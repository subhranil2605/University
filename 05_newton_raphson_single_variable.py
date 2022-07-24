"""
Newton Raphson Method in Python
"""
from sympy import Symbol, diff, lambdify, sympify
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('classic')


def derivative(expression):
    x = Symbol('x')  
    f = lambdify(x, (func_ := sympify(expression)))
    f_prime = lambdify(x, (func_p_ := diff(expression)))
    print(f"The function is: {func_}")  
    print(f"The derivative of the function is: {func_p_}")
    return f, f_prime


def newton_raphson(func, appx_root, err = 0.01, max_iter = 10):
    f, f_prime = derivative(func)
    root = None
    print("\nn\t|x_n\t\t|f(x_n)\t\t|x_(n+1)\t|h\t\t\t|")
    roots = []
    for i in range(max_iter + 1):
        new_root = appx_root - (h := f(appx_root) / f_prime(appx_root))

        if abs(h) <= err:
            root = new_root  
            print(f"{i}\t|{appx_root:0.5f}\t|{f(appx_root):0.5f}\t|{new_root:0.5f}\t|{h:0.5f}\t|")
            break
        else:
            print(f"{i}\t|{appx_root:0.5f}\t|{f(appx_root):0.5f}\t|{new_root:0.5f}\t|{h:0.5f}\t|")
            appx_root = new_root  
        roots.append(new_root)

    return root if root else "\nInsufficient Iteration!!!", roots


if __name__ == '__main__':
##    func = "cos(x)-exp(x)"
##    def f(x):
##        return np.cos(x) - np.exp(x)

    func = "x**3-2*x**2+x+0.5"

    def f(x):
        return x**3-2*x**2+x+0.5

    for i in range(10):
        result = newton_raphson(func, 2.1, 0.0001, i)
        if result[0] != "\nInsufficient Iteration!!!":
            print(f"\nThe root is: {result[0]}")
            break

    y = [f(i) for i in result[1]]
    print(y)

    # plotting 
    plt.plot((x := np.linspace(-5, 6, 100000)), f(x), label="f(x)")
    
    plt.plot(result[1], y)
    plt.plot(result[1], y, '.', label="x")
    
    plt.axhline(0, color='red', alpha=0.5)
    plt.axvline(0, color='red', alpha=0.5)
    
    plt.xlabel("$x$")
    plt.ylabel("$f(x) = cos(x)-e^x$")
    
    plt.xticks(range(-5, 6))

    plt.xlim(-5, 6)
    plt.ylim(-5, 4)
    
    plt.legend()
    plt.show()
