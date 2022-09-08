import numpy as np
import math

INFINITY: int = 100


def ex(val, n=None):
    result: int = 0

    for i in range(n or INFINITY):
        result += np.power(val, i) / math.factorial(i)

    return result


def truncation_error(val, break_point=None):
    actual_value: float = ex(val)
    break_point = break_point or int(input('Enter the point where do you want to break: '))
    appx_value: float = ex(val, break_point)
    truncated_error: float = actual_value - appx_value
    return actual_value, appx_value, truncated_error


if __name__ == '__main__':
    # taking the value from the user
    x: float = float(input("Enter the value of x: "))

    # calling the truncation_error function to get the values
    true_value, appx_value, truncated_error = truncation_error(x)

    # printing the truncated error
    print(f"Truncation error is: {truncated_error:.5f}")
