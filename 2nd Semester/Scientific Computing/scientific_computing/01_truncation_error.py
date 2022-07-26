import numpy as np

INFINITY: int = 100


def factorial(n: int) -> int:
    '''
    calculate factorial
    
    :param n: the number to get its factorial
    '''
    
    result: int = 1
    for i in range(1, n + 1):
        result *= i
        
    return result


def ex(val: float, n: int = None) -> float:
    '''
    e^x function
    
    :param val: value to be calculated
    :param n: optional value, where to truncate the series
    '''
    result: int = 0
    
    for i in range(n or INFINITY):
        result += np.power(val, i) / factorial(i)
        
    return result


def truncation_error(val: float, break_point: int = None) -> tuple[float,...]:
    '''
    Calculate the truncation error with the given function

    :param val: value to be calculated
    :param break_point: point where to be truncated
    '''
    
    actual_value: float = ex(val)
    break_point = break_point or int(input('Enter the point where do you want to break: '))
    appx_value: float = ex(val, break_point)
    truncated_error: float = actual_value - appx_value
    return actual_value, appx_value, truncated_error
    


if __name__ == '__main__':
    # taking the value from the user
    x: float = float(input("Enter the value of x: "))

    # calling the truncation_error function to get the values
    true_value, appx_value, truncated_error =  truncation_error(x)

    # printing the truncated error
    print(f"Truncation error is: {truncated_error:.5f}")

    
