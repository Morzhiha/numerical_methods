from sympy import symbols, cos, sin

n = 7
a = 1
b = 2
y0 = 1
x0 = a
eps = 0.00001
x, y = symbols('x y')

def f(x, y):
    return y/x + x * cos(x)

def runge_kutta(N):
    h = (b-a)/N
    X = [a+i*h for i in range(N)]
    Y = [y0 for i in range(N)]
    phi = [0]*4
    for i in range(N-1):
        phi[0] = h * f(X[i], Y[i])
        phi[1] = h * f(X[i] + h / 2, Y[i] + phi[0] / 2)
        phi[2] = h * f(X[i] + h / 2, Y[i] + phi[1] / 2)
        phi[3] = h * f(X[i] + h, Y[i] + phi[2])
        Y[i+1] = Y[i] + 1 / 6 * (phi[0] + 2 * phi[1] + 2 * phi[2] + phi[3])
    return Y[N-1]
N = 20
Yh = runge_kutta(N)
N = 2*N
Yh2 = runge_kutta(N)
print(Yh, Yh2)

m = 4
delta = (Yh2 - Yh) / (2**m - 1)
while(abs(delta) > eps):
  Yh = Yh2
  N = 2 * N
  Yh2 = runge_kutta(N)
  delta = (Yh2 - Yh) / (2**m - 1)
  print(Yh, Yh2)

print("Метод Рунге-Ромберга ", Yh2+delta)

def F(x):
    return x * sin(x) + x * (1 - sin(1))
h = (b-a)/N
X = [a + i * h for i in range(N)]
print(F(x).subs(x, b).evalf())
print(F(x).subs(x, b).evalf() - Yh2+delta)