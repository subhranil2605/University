from typing import Callable
import numpy as np
from tabulate import tabulate


# secant method function
def secant(func: Callable[[float], float],
           point_1: float,
           point_2: float,
           e: float = 0.001) -> tuple[float, list]:
    """
    Secant method in python
    """
    s: list = []
    iteration: int = 0
    while (err := abs(point_2 - point_1)) >= e:
        f_point_1: float = func(point_1)
        f_point_2: float = func(point_2)

        root: float = (point_1 * f_point_2 - point_2 * f_point_1) / (f_point_2 - f_point_1)

        # for table
        s.append([iteration + 1, point_1, point_2, root, err])

        # updating values
        point_1 = point_2
        point_2 = root

        iteration += 1
    return round(root, 5), s


if __name__ == '__main__':
    # user function
    user_func: Callable[[float], float] = lambda x: x * np.exp(x) - 1

    # arbitrary points
    user_point_1: float = 0.0
    user_point_2: float = 1.0

    # tolerance level
    user_e: float = 0.001

    # calling secant method
    result: tuple[float, list] = secant(user_func, user_point_1, user_point_2, user_e)

    print("The root is: ", result[0])
    print()
    table = result[1]
    header = ["n", "point_1", "point_2", "root", "error"]
    print(tabulate(table, header, tablefmt="grid"))
