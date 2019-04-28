import numpy as np
from scipy import integrate
from math import exp
from math import sqrt

q = [100.001278, 121.2209058, 11.75831995, 12.59081308]
mu1 = 100.001278
mu2 = 121.2209058
sigma1 = 11.75831995
sigma2 = 12.59081308
f = lambda x,y :(-0.5) * ( ((x-mu1)**2)/sigma1 + ((y-mu2)**2)/sigma2
# f = lambda z : 1/(sigma1*sigma2*2))

# r =200
g = lambda x: 0
h = lambda y: (sqrt(r**2-y**2)

i = integrate.dblquad(f,-200,200,g,h)
print(i)

# f = lambda x, y : 16*x*y
# g = lambda x : 0
# h = lambda y : sqrt(1-4*y**2)
# i = integrate.dblquad(f, 0, 0.5, g, h)
# print (i)