"""
Method of False Position
also known as Regula-falsi
"""
from typing import Callable, Any
from tabulate import tabulate


def regula_falsi(func: Callable[[float], float], point_1: float, point_2: float, err: float) -> Any:
    """
    Regula falsi method
    """
    if func(point_1) * func(point_2) >= 0:
        print(f"There's no root in between {point_1} and {point_2}")
        return None
    else:
        n: int = 0
        s: list = []
        while abs(f_r := (
                func(root := (point_1 * (f_point_2 := func(point_2)) - point_2 * (f_point_1 := func(point_1))) / (
                        f_point_2 - f_point_1)))) >= err:
            if f_r * f_point_1 < 0:
                s.append([n, point_1, point_2, f_point_1, f_point_2, root, f_r])
                point_2 = root
            elif f_r * f_point_2 < 0:
                s.append([n, point_1, point_2, f_point_1, f_point_2, root, f_r])
                point_1 = root
            n += 1

        return root, s


if __name__ == '__main__':
    func: Callable[[float], float] = lambda x: x ** 3 - x ** 2 + 2
    result = regula_falsi(func, -5.0, 5.0, 0.01)
    print(f"root is {result[0]}")
    table = result[1]
    header = ["n", "a", "b", "f(a)", "f(b)", "root", "f(root)"]
    print(tabulate(table, header, tablefmt="github"))
