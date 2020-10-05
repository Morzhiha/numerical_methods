from sympy import symbols, sin, diff
from scipy import integrate

n = 7
eps = 0.001
a = 0.2*(n + 6)
b = 0.3*(n + 6)

x = symbols('x')

def f(x):
  return 1/(x + sin(0.1*n*x))

def f1(x):
  return diff(f(x), x)

N = 1
h = (b-a)/N
X = [a+i*h for i in range(N)]

Yh = sum(h*(f(a+(i-1)*h)+4*f((a+i*h+a+(i-1)*h)/2)+f(a+i*h))/6 for i in range(1, N+1))
N = 2*N
h = h / 2
X = [a+i*h for i in range(N)]
Yh2 = sum(h*(f(a+(i-1)*h)+4*f((a+i*h+a+(i-1)*h)/2)+f(a+i*h))/6 for i in range(1, N+1))
print(Yh)
print(Yh2)

m = 4
delta = (Yh2 - Yh) / (2**m - 1)
while(abs(delta) > eps):
  Yh = Yh2
  N = 2 * N
  h = h / 2
  X = [a + i * h for i in range(N)]
  Yh2 = sum(h*(f(a+(i-1)*h)+4*f((a+i*h+a+(i-1)*h)/2)+f(a+i*h))/6 for i in range(1, N+1))
  print(Yh, Yh2)
  delta = (Yh2 - Yh) / (2**m - 1)

print("I1 ", Yh2+delta)

print(integrate.quad(lambda x: f(x), a, b))
