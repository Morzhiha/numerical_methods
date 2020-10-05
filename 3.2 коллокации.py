import matplotlib.pyplot as plt
from sympy import *
import numpy as np

n = 7

a = 0
b = pi
alpha = 0
beta = 2
gamma = 0
delta = 1
A = -1
B = -2
x = symbols('x')

def p(x):
    return sin(x)
def q(x):
    return sin(2*x)
def f(x):
    return exp(x)

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
for i in range(N):
    for j in range(N):
        aa[i][j] = diff(phi[j], x, x).subs(x, X[i])\
                   + p(X[i]) * diff(phi[j], x).subs(x, X[i])\
                   + q(X[i]) * (phi[j]).subs(x, X[i])
    bb[i] = f(x).subs(x, X[i]) - diff(phi[0], x, x).subs(x, X[i]) \
            - p(X[i]) * diff(phi[0], x).subs(x, X[i]) \
            - q(X[i]) * (phi[0]).subs(x, X[i])
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
