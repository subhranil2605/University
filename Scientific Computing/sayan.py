from sympy import *
import numpy as np

def Jacobian(v_str, f_list):
    var = symbols(v_str)
    f = sympify(f_list)
    J = zeros(len(f),len(var))
    for i, fi in enumerate(f):
        for j, s in enumerate(var):
            J[i,j] = diff(fi, s)        
    return J


x, y = symbols('x y')

f_xy = x**2 + x*y + y*y - 7
g_xy = x**3 + y**3 - 9
ja = Jacobian('x y',[f_xy, g_xy])
ja_1 = ja.inv()

a_n = 1.5
b_n = 0.5
n = 10

for i in range(n):
  x_y_dict = {'x': a_n, 'y': b_n}
  
  ja_inverse = ja_1.subs(x_y_dict)
  
  f_matrix = Matrix([
      [f_xy.subs(x_y_dict)],
      [g_xy.subs(x_y_dict)]
  ]).subs(x_y_dict)
  
  f1 = np.array([[a_n], [b_n]])
  
  result = f1 - np.dot(ja_inverse, f_matrix)
  a_n, b_n = result[0, 0], result[1, 0]

  print('IN THE FINAL ANSWER THE a will be: ', a_n)
  print('IN THE FINAL ANSWER THE b will be: ', b_n) 
 
