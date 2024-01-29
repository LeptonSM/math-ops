import numpy as np 

n = 10 
x = []
y = []
_sum = []

for i in range(n): 
   x.append(i)
   y.append(0.5*i)   

_sum = np.add(x, y)
for i in range(n):
   print(i, x[i], y[i], _sum[i])
   
_multiply = np.multiply(x,y)
for i in range(n):
   print(i, x[i], y[i], _multiply[i])
   
