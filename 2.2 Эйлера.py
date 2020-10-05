from sympy import symbols
import matplotlib.pyplot as plt
from scipy.integrate import odeint

NN = 6
a = 1
b = 2
y0 = 1
x0 = a
N = 10
h = (b-a)/N
X = [a+i*h for i in range(N)]
x = symbols('x')

def f(x_, y):
    return -(1 + x_*y) / x_**2

Y = [y0 for i in range(N)]
for i in range(N-1):
    Y[i+1] = Y[i] + h * f(X[i], Y[i])
print(Y)
print(X)
# sol = odeint(f, y0, X)
# print(len(sol))

fig = plt.figure()
plt.plot(X, Y, 'ro')
# plt.plot(X, sol)
plt.show()
plt.close(fig)
