from sympy import *
import numpy as np

def Jacobian(v_str, f_list):
    vars = symbols(v_str)
    f = sympify(f_list)
    J = zeros(len(f),len(vars))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            J[i,j] = diff(fi, s)        
    return J


x, y = symbols('x y')
f = x**2 + x*y + y*y - 7
g = x**3 + y**3 - 9

# ------------
a, b = 1.5, 0.5
for i in range(5):
    X = Matrix([[a],[b]])

    F = Matrix([
        [f.subs({'x': a, 'y': b})],
        [g.subs({'x': a, 'y': b})]
    ])

    ja = Jacobian('x y', [f, g])

    ja_inv = ja.inv().subs({'x': a, 'y': b})

    result = X - np.dot(ja_inv, F)
    a, b = result[0, 0], result[1, 0]

print(result)

