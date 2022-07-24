from typing import Callable, Any
import matplotlib.pyplot as plt

function_type = Callable[[float], float]

def regula_falsi(func: function_type,
                 point_1: float,
                 point_2: float,
                 err: float = 0.001,
                 max_iter: int = 10) -> Any:
    """
    Regula Falsi method
    """
    
    if func(point_1) * func(point_2) > 0:
        return None
    else:
        roots = []
        for _ in range(max_iter):
            nume: float = point_1 * (f_2 := func(point_2)) - point_2 * (f_1 := func(point_1))
            den: float = f_2 - f_1
            root: float = nume / den
            f_r: float = func(root)
            
            if f_r >= err:
                if f_r * f_1 < 0:
                    point_2 = root
                elif f_r * f_2 < 0:
                    point_1 = root
            else:
                break
            
            roots.append(root)
        return root, roots


if __name__ == '__main__':
    a, b = -2.0, 0.0
    e = 0.0000000000000001
    m_iter = 6

    result = regula_falsi(lambda x: x ** 3 - x ** 2 + 2, a, b, e, m_iter)

    if result:
        print(f"Approximated root: {result[0]:0.6f}\nafter iterations: {len(result[1])}\nfor tolerance error: {e}")
        plt.plot(result[1])
        plt.show()
    else:
        print(f"There's no root in between {a} and {b}")
