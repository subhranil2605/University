"""
Subhranil Sarkar
Assignment 1
Python 3.10.4
"""

import numpy as np


INFINITY: int = 100
str_float_dict = dict[str, float]


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


def errors(true_value: float,
           approx_value: float,
           round_digit: int) -> str_float_dict:
    '''
    Calculate abs error, rel error and percn error upto given significant digits

    :param true_value: actual value
    :param approx_value: approximated value
    :param round_digit: round off value
    '''
    
    absolute_error: float = round(abs(true_value - approx_value), round_digit)      # absolute error
    relative_error: float = round(absolute_error / true_value, round_digit)         # relative error
    percentage_error: float = round(relative_error * 100, round_digit)              # percentage error

    # creating a dictionary to store all the errors 
    result: str_float_dict =  {
        "absolute_error": absolute_error,
        "relative_error": relative_error,
        "percentage_error": percentage_error
    }

    return result
    


if __name__ == '__main__':
    # taking the value from the user
    x: float = float(input("Enter the value of x: "))

    # calling the truncation_error function to get the values
    true_value, appx_value, truncated_error =  truncation_error(x)

    # other errors 
    calc_errors: str_float_dict = errors(true_value, appx_value, 5)

    # printing the truncated error
    print(f"Truncation error is: {truncated_error:.5f}")

    # printing the other errors using list comprehension
    [print(f"{key} = {value}") for key, value in calc_errors.items()]

    
