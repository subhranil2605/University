"""
Newton Raphson Method in Python
"""
from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly


# plt.style.use('fivethirtyeight')


def derivative(func, x) -> tuple[Any, Any]:
    """
    Calculate the derivative expression from an expression
    given by user and returns both of them
    """
    return np.gradient(func(x), x)


def newton_raphson(func: list, appx_root: float, err: float = 0.01, max_iter: int = 10) -> Any:
    """
    Calculates Newton-Raphson Method
    """
    
    root = None

    roots = []
    for i in range(max_iter + 1):
        h = func(appx_root) / derivative(func, appx_root)
        new_root = appx_root - h
        if abs(h) <= err:
            root = new_root 
            break  
        else:
            appx_root = new_root  
        roots.append(new_root)

    return root, roots if root else "\nInsufficient Iteration!!!"


if __name__ == '__main__':
    # the function is cos(x) - e**x
    func: list = lambda x: np.cos(x) -  np.exp(x)

    result: Any = newton_raphson(func, 2.0, 0.0000000001, 10)
    print(f"\nThe root is: {result[0]}")


##    y = list(map(lambda x: np.cos(x) - np.exp(x), result[1]))
##    print(y)



