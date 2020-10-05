from sympy import symbols, Interval
from sympy.calculus.util import maximum
from scipy import integrate
import math

NN = 6
eps = 0.001
a = 0.1*(NN+3)
b = 0.25*(NN+3)
print('a =', a,', b =', b)

x = symbols('x')

def f(x):
  return 1/x*pow(math.e, 0.01*NN*x)

def f1(x):
  return (0.06 * pow(math.e, 0.01 * NN * x) / x - pow(math.e, 0.01 * NN * x) / (x * x))

def f2(x):
  return (0.0036 * pow(math.e, 0.01 * NN * x) / x - 0.12 * pow(math.e, 0.01 * NN * x) / (x * x) + 2 * pow(math.e, 0.01 * NN * x) / ( x*x*x))

M1 = max(abs(maximum(f1(x), x, Interval(a, b))), abs(maximum(-f1(x), x, Interval(a, b))))
print('max ', M1)
h = (2 * eps) / (b - a) * M1
print('шаг =', h)

N = math.ceil((b - a) / h)
print('Количество узлов =', N)

y = lambda x : f(x)
#print(integrate.quad(y,a,b))

print('Формула правых прямоугольников ', sum(h * f(a + i * h) for i in range(0, N - 1)))
print('Формула левых прямоугольников ', sum(h * f(a + i * h) for i in range(1, N)))

M2 = maximum(f2(x), x, Interval(a, b))

h = math.sqrt((24 * eps) / ((b - a) * M2))
print('шаг =', h)

N = math.ceil((b - a) / h)
print('Количество узлов =', N)

print('Формула средних прямоугольников ', sum(h * f((a + i*h + a + (i - 1)*h) / 2) for i in range(1, N)))

print(integrate.quad(lambda x: 1/x * pow(math.e, 0.01*NN*x), a, b))