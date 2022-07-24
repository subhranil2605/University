from typing import Callable
import numpy as np


# secant method function
def secant(func: Callable[[float], float],
           point_1: float,
           point_2: float,
           e: float = 0.001) -> tuple[float, str]:
    """
    Secant method in python
    """
    s: str = "n\t|point_1\t\t|point_2\t\t|root\t\t|error\t\t|\n"
    iteration: int = 0
    while (err := abs(point_2 - point_1)) >= e:
        f_point_1: float = func(point_1)
        f_point_2: float = func(point_2)

        root: float = (point_1 * f_point_2 - point_2 * f_point_1) / (f_point_2 - f_point_1)

        # for table
        s += f"{iteration + 1}\t|{point_1:0.5f}\t\t|{point_2:0.5f}\t\t|{root:0.5f}\t|{err:0.5f}\t|\n"

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
    result: tuple[float, str] = secant(user_func, user_point_1, user_point_2, user_e)

    print("The root is: ", result[0])
    print()
    print(result[1])
