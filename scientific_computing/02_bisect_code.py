"""
Subhranil Sarkar
Bisection code
"""

from typing import Callable, Any
import numpy as np
from tabulate import tabulate


# bisection function
def bisection(func: Callable[[float], float],
              a: float,
              b: float,
              e: float = 0.001,
              verbose: bool = False) -> Any:
    '''
    bisection method to calculate root between two values
    '''
    if func(a) * func(b) >= 0:  # intermediate theorem invalid here
        print(f"There is no root in between {a} and {b}")
        return None

    else:
        s = []
        while abs(b - a) >= e:
            if func((root := (a + b) / 2.0)) == 0:  # exact root
                return root
            elif (f_r := func(root)) * (f_a := func(a)) < 0:  # root lies in between (a, root)
                s.append([a, b, f_a, func(b), root, f_r])
                b = root
            else:  # root lies in between (root, b)
                s.append([a, b, f_a, func(b), root, f_r])
                a = root

        # return table 
        if verbose:
            return {"root": root, "table": s}

        # return root only
        return root


if __name__ == "__main__":
    a_value = 0.0
    b_value = 1.0
    tolerance_level = 0.01
    verbose = True
    root = bisection(lambda x: np.power(x, 4) - 5 * x + 1, a_value, b_value, tolerance_level, verbose)

    if verbose:
        print(f"The root is = {root['root']}")
        print("\nBisection Method\n")

        h = ["a", "b", "f(a)", "f(b)", "root", "f(root)"]
        table = root["table"]
        print(tabulate(table, h, showindex="always", tablefmt="grid"))

    else:
        print(f"The root is = {root}")
