import matplotlib.pyplot as plt
from sympy import *
import numpy as np
# from scipy import integrate

NN = 6

a = 1
b = 2
alpha = 1
beta = -3
gamma = 2
delta = 1
A = -6
B = 1
x = symbols('x')

def p(x):
    return 2/sqrt(x)
def q(x):
    return x
def f(x):
    return 1/x

N = 5
h = (b-a)/N
X = [a+i*h for i in range(N)]

N = 5
h = (b-a)/N
X = [a+i*h for i in range(N)]
# будем искать phi = c*x + d
c, d = symbols('c d')
phi = [0]*N
s = solve([alpha*c + beta*(c*a + d) - A, delta*c + gamma*(c*b + d) - B], [c, d])
phi[0] = s[c] * x + s[d]

aa = np.zeros((N, N))
bb = np.zeros(N)

for i in range(1, N):
    pi = -(((b-a)*(delta*(i+2) + gamma*(b-a)))/(delta*(i+1) + gamma*(b-a)))
    phi[i] = pi*(x - a)**(i+1) + (x-a)**(i+2)
print("phi", phi)
def L(x, u):
    return diff(u, x, x) + p(x)*diff(u, x) + q(x)*(u)

for i in range(N):
    for j in range(N):
        aa[i][j] = integrate(L(x, phi[i])*phi[j], (x, a, b))
    bb[i] = integrate((f(x) - L(x, phi[0]))*phi[i], (x, a, b))
    print(aa)
    print(bb)

def SLAU(aa, bb):
    nn = N
    L = np.eye(nn)
    U = np.zeros((nn, nn))
    for i in range(nn):
        for j in range(nn):
            if (i <= j):
                U[i, j] = aa[i, j] - sum((L[i, k] * U[k, j]) for k in range(i))
            if (i > j):
                L[i, j] = (aa[i, j] - sum((L[i][k] * U[k][j]) for k in range(j))) / U[j, j]
    y = np.zeros(nn)
    for k in range(nn):
        y[k] = bb[k] - sum((L[k, j] * y[j]) for j in range(k))

    x = np.zeros(nn)
    for k in range(nn - 1, -1, -1):
        x[k] = (y[k] - sum((U[k, j] * x[j]) for j in range(k, nn))) / U[k, k]

    return x

c = SLAU(aa, bb)
print("c", c)

y = phi[0] + sum([c[i] * phi[i] for i in range(N)])
print(y)

fig = plt.figure()
plt.plot(X, [y.subs(x, X[i]) for i in range(N)], )
plt.show()