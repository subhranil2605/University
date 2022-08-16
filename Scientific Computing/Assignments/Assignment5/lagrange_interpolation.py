"""
Lagrange Interpolation
Subhranil Sarkar

packages used:
    pip install tabulate
"""

from tabulate import tabulate


def lagrange_func(x_values: list, y_values: list, x) -> int | float:
    """
    Lagrange Interpolation

    :param x_values: list of the given data points
    :param y_values: list of the other data points
    :param x: value given
    :raises AssertionError: if the length of the two lists do not match
    :retuns: calculated value for x
    """
    
    assert len(x_values) == len(y_values), "Length of the two lists should be same!!!"

    # to store the result 
    result = 0
    
    for i, y_val in enumerate(y_values):
        l_i = y_val
        for j in range(len(x_values)):
            if j != i:
                l_i *= (x - x_values[j]) / (x_values[i] - x_values[j])  # formula
                
        result += l_i

    return result


if __name__ == "__main__":
    x_vals: list = [300, 304, 305, 307]
    y_vals: list = [2.4771, 2.4829, 2.4843, 2.4871]
    
    x: int = 301
    
    table: list[list] = [[i, j] for i, j in zip(x_vals, y_vals)]
            
    y: int | float = lagrange_func(x_vals, y_vals, x)

    print(tabulate(table, headers=["X", "Y"], showindex="always", tablefmt="pretty"))
    
    print(f"For X: {x} the value of Y: {y:0.6f}")
    
