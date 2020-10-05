from sympy import symbols, exp, oo, integrate, sqrt, ceiling, diff, Interval
from sympy.calculus.util import maximum

n = 7
k = 0
eps = 0.001
a = 0.1 * n
# b = 0.1 * n

x = symbols('x')

def f(x):
  return x**(k + 2) * exp(- x**2)

b = a
I = abs(integrate(f(x), (x, b, +oo)))
while ( I > eps/2):
  b += b
  I = abs(integrate(f(x), (x, b, +oo)))
print("b = ", b)
# используем формулу средних прямоугольников
M2 = max(maximum(diff(f(x), x, 2), x, Interval(a, b)), maximum(-diff(f(x), x, 2), x, Interval(a, b))).evalf()
print(M2)

h = sqrt((24*eps)/((b-a)*M2))
print('шаг =', h)

N = ceiling((b-a)/h)
print('Количество узлов =', N)

X = [a]
I1 = 0

for i in range(1, N):
  X.append(a + i*h)
  I1 += h*f((X[i]+X[i-1])/2)

print("Интеграл", I1)

print(integrate(f(x), (x, a, oo)).evalf())
