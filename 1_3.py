from sympy import symbols, Interval, diff,exp
from sympy.calculus.util import maximum, minimum
from scipy import integrate,optimize
import math

NN = 6
eps = 0.001
a = 0.1*(NN+3)
b = 0.25*(NN+3)
print('a =',a,', b =',b)

x = symbols('x')

def f(x):
  return 1/x*exp(-0.01*NN*x**(3/2))

def f1(x):
  return diff(f(x),x)

def f2(x):
  return diff(f1(x),x)

def f4(x):
  return diff(diff(f2(x),x),x)

#print(minimum(f2(x),x,Interval(a,b)))
#M4 = optimize.fminbound(-f4(x),a,b)

# вместо вычисления максимума 4ой  производной на интервале просто подставили левую границу(посмотрели по графику)
M4 = f4(x).subs(x,a)

h = pow((2880*eps)/((b-a)*M4),1/4)
print('шаг =',h)

N = math.ceil((b-a)/h)
print('Количество узлов =', N)

h = (b-a)/N

print('Формула Симпсона', sum(h*(f(a+(i-1)*h)+4*f((a+i*h+a+(i-1)*h)/2)+f(a+i*h))/6 for i in range(1,N+1)))

print(integrate.quad(lambda x: 1/x*exp(-0.01*NN*x**(3/2)), a, b))