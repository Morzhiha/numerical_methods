from sympy import symbols, diff, sin
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

def C(x, i):
  return integrate.quad(lambda x: w(x, i)/w1(x, i), a, b)

N = 5
h = (b-a)/N
X = [a+i*h for i in range(N)]

I1 = 0
for i in range(N):
  I1 += integrate.quad(lambda x: w(x, i) / w1(x, i), a, b)[0] * f(X[i])

print('I1 ', I1)

print(integrate.quad(lambda x: f(x), a, b))

def M(N):
  return diff(f(x), x, N).subs(x, a)

print("r <= ", M(N+1)/factorial(N+1) * integrate.quad(lambda x: abs(w(x,-1)), a, b)[0])