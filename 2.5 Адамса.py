from sympy import symbols
import matplotlib.pyplot as plt

NN = 6
a = 1
b = 2
y0 = 1
x0 = a

x = symbols('x')

def f(x_, y):
    return -(1 + x_*y) / x_**2

N = 10
h = (b-a)/N
X = [a+i*h for i in range(N)]
Y = [y0 for i in range(N)]
phi = [0]*4
for i in range(4):
    phi[0] = h * f(X[i], Y[i])
    phi[1] = h * f(X[i] + h / 2, Y[i] + phi[0] / 2)
    phi[2] = h * f(X[i] + h / 2, Y[i] + phi[1] / 2)
    phi[3] = h * f(X[i] + h, Y[i] + phi[2])
    Y[i+1] = Y[i] + 1 / 6 * (phi[0] + 2 * phi[1] + 2 * phi[2] + phi[3])

for i in range(3, N-1):
    Y[i+1] = Y[i] + h/24*(55*f(X[i],Y[i]) - 59*f(X[i-1],Y[i-1]) + 37*f(X[i-2],Y[i-2]) - 9*f(X[i-3],Y[i-3]))
print(Y)
print(X)

fig = plt.figure()
plt.plot(X, Y, 'ro')
plt.show()
plt.close(fig)
