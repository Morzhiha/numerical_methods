from sympy import symbols, diff, sin
from scipy import integrate
import numpy as np

n = 7
eps = 0.001
a = 0.2*(n + 6)
b = 0.3*(n + 6)

x = symbols('x')

def f(x):
  return 1/(x + sin(0.1*n*x))

def f1(x):
  return diff(f(x), x)

N = 50
h = (b - a) / N
X = [a + i * h for i in range(N)]

A = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        if (i == j):
            A[i][j] = 4 * h / 6
        if (i == j-1) or (i == j+1):
            A[i][j] = h / 6
B = np.zeros(N)
for i in range(1, N-1):
  B[i] = (f(X[i+1])-f(X[i]))/h - (f(X[i])-f(X[i-1]))/h
m = np.linalg.solve(A, B)
# print(m)

def S3(i):
  return -m[i]/(6*h)*(x - X[i+1])**3 + m[i+1]/(6*h)*(x-X[i])**3 + ((f(X[i+1])-f(X[i]))/h - h/6*(m[i+1]-m[i]))*(x-X[i]) + f(X[i])-m[i]/6*(h)**2


print('I1', 5 * h / 12 * (f(X[0]) + f(X[N - 1])) + 13 * h / 12 * (f(X[1]) + f(X[N - 2])) + h * sum(f(X[i]) for i in range(2, N - 2)) - h ** 3 / 72 * (2 * m[0] + m[1] + m[N - 2] + 2 * m[N - 1]))

print(integrate.quad(lambda x: f(x), a, b))