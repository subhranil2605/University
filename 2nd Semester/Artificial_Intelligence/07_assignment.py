import numpy as np
from numpy import ndarray
from typing import Callable




# objective function
def func_xy(x, y):
    return x * (x - 4) + y * (y - 5) 


# partial derivative wrt x
def x_deriv(x):
    return 2 * x - 4


# partial derivative wrt y
def y_deriv(y):
    return 2 * y - 5


def gradient_descent(x_start: float,
                     y_start: float,
                     func: Callable[[float, float], float],
                     learn_rate: float,
                     max_iter: int,
                     tol: float = 0.01) -> tuple[list[float], float]:
    """
    Gradient Descent algorithm implementation

    :param x_start: starting piont of x
    :param y_start: starting piont of y
    :param func: objective function
    :param learn_rate: learning rate of the algorithm
    :param max_iter: max iteration
    :param tol: tolerance level
    """

    # Store x, y values to plot the data
    steps = [[x_start, y_start]]

    for _ in range(max_iter):
        x_diff: float = learn_rate * x_deriv(x_start)
        y_diff: float = learn_rate * y_deriv(y_start)

        if np.abs(x_diff) < tol and np.abs(y_diff) < tol:
            break

        x_start -= x_diff
        y_start -= y_diff

        steps.append([x_start, y_start])

    return x_start, y_start, steps



def plot_data(steps):
    from mpl_toolkits import mplot3d
    import matplotlib.pyplot as plt
    
    x = y = np.linspace(-20, 20, 30)
    X, Y = np.meshgrid(x, y)
    Z = func_xy(X, Y)

    fig = plt.figure(figsize=(8, 12))

    ax = fig.add_subplot(2, 2, 1, projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    x_s = [step[0] for step in steps]
    y_s = [step[1] for step in steps]
    z_s = [func_xy(i, j)  for i, j in zip(x_s, y_s)]


    ax = fig.add_subplot(2, 2, 2, projection='3d')
    ax.view_init(12, 40)
    ax.scatter(x_s, y_s, z_s, c=z_s, cmap='viridis', linewidth=0.5);
    ax.plot3D(x_s, y_s, z_s)



    ax = fig.add_subplot(2, 2, 3, projection='3d')
    ax.scatter(x_s, y_s, z_s, c=z_s, cmap='viridis', linewidth=0.5);
    ax.plot3D(x_s, y_s, z_s)
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$f(x,y)=x(x-4)+y(y-5)$')
    ax.set_title('Gradient Descent')


    plt.show()


if __name__ == "__main__":
    lower_bound = -20.0
    upper_bound = 20.0

    lr = 0.8

    # random starting point
    x_starting_point = np.random.randint(lower_bound, upper_bound)
    y_starting_point = np.random.randint(lower_bound, upper_bound)

    # result
    x, y, steps = gradient_descent(x_starting_point, y_starting_point, func_xy, lr, 100)

    min_value: float = func_xy(x, y)
    
    print(f"The minimum value is: {min_value:0.5f}")
    print(f"And corresponding values of x and y are {x = } and {y = }")

    plot_data(steps)





