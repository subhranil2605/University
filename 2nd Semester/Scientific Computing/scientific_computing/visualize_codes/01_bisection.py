"""
Subhranil Sarkar
Bisection code
"""

from typing import Callable, Any
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# function for the equation
def func(x):
    return np.power(x, 4) - 5 * x + 1


# bisection function
def bisection(func: Callable[[float], float],
              a: float,
              b: float,
              e: float = 0.001,
              verbose: bool = False) -> Any:
    '''
    bisection method to calculate root between two values
    '''
    
    if func(a) * func(b) >= 0:                                                                              # intermediate theorem invalid here
        print(f"There is no root in between {a} and {b}")
        return None

    else:
        s = []
        while abs(b - a) >= e:
            if func((root := (a + b) / 2.0)) == 0:                                                          # exact root
                return root
            elif (f_r := func(root)) * (f_a := func(a)) < 0:                                                # root lies in between (a, root)
                # s.append([a, b, f_a, func(b), root, f_r])
                s.append([a, b, root])
                b = root
            else:                                                                                           # root lies in between (root, b)
                # s.append([a, b, f_a, func(b), root, f_r])
                s.append([a, b, root])
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
    root = bisection(func, a_value, b_value, tolerance_level, verbose)
    # print(f"The root is = {root['table']}")

    h = np.array(root['table'])
    print(h)

##    offset = 1
##    x_val = np.linspace(a_value - offset, b_value + offset, 1000)
##    y_val = func(x_val)
##    plt.plot(x_val, y_val)
##    plt.axhline(color="red", alpha=0.5)
##    plt.axvline(color="red", alpha=0.5)
##    plt.show()
    
