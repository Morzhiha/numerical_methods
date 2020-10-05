from sympy import symbols, diff, sin
from sympy.solvers import solve
from scipy import integrate
from math import factorial

n = 7
eps = 0.001
a = 0.2*(n + 6)
b = 0.3*(n + 6)

x = symbols('x')

def f(x):
  return 1/(x + sin(0.1*n*x))

def f1(x):
  return diff(f(x),x)

def w(x,i):
  ww = 1
  for g in range(N):
    if g != i:
      ww *= (x - X[g])
  return ww

def w1(x,i):
  ww = 1
  for g in range(N):
    if g != i:
      ww *= (X[i] - X[g])
  return ww

def C(i):
  return integrate.quad(lambda x: w(x, i)/w1(x, i), a, b)[0]

N = 10
h = (b-a) / N

P = 1/(2**N * factorial(N)) * diff((x**2 - 1)**N, x, N)
pn = solve(P, x)

X = [(b-a)/2*pn[i] + (b+a)/2 for i in range(N)]

I1 = 0
for i in range(N):
  I1 += C(i)*f(X[i])

print('Формула Гаусса', I1)

print(integrate.quad(lambda x: f(x), a, b))
