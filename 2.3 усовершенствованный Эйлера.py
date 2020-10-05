from sympy import symbols, solvers
import matplotlib.pyplot as plt

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
Y_ = [y0 for i in range(N)]
for i in range(N-1):
    Y_[i+1] = Y[i] + h * f(X[i], Y[i])
    Y[i+1] = Y[i] + h/2 * (f(X[i], Y[i]) + f(X[i+1], Y_[i+1]))

print(Y)
print(X)
fig = plt.figure()
plt.plot(X, Y, 'ro')
plt.show()
plt.close(fig)
