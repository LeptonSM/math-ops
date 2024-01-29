import numpy as np

x = []
y = []
_quo = []

n = 10

for i in range(n): 
   x.append(i)
   y.append(0.5*i)   

_quo = np.divide(x, y)

for i in range(n):
   print(i, x[i], y[i], _quo[i])
   

