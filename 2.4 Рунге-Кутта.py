from numpy.ma import arange
from sympy import symbols
import matplotlib.pyplot as plt
from scipy.integrate import odeint, ode

NN = 6
a = 1
b = 2
y0 = 1
x0 = a

x = symbols('x')

def f(x_, y):
    return -(1 + x_*y) / x_**2

N = 10
h = (b-a)/N
X = [a+i*h for i in range(N)]
Y = [y0 for i in range(N)]
phi = [0]*4
print(phi)
for i in range(N-1):
    phi[0] = h * f(X[i], Y[i])
    phi[1] = h * f(X[i] + h / 2, Y[i] + phi[0]/2)
    phi[2] = h * f(X[i] + h / 2, Y[i] + phi[1] / 2)
    phi[3] = h * f(X[i] + h, Y[i] + phi[2])
    Y[i+1] = Y[i] + 1/6*(phi[0] +2*phi[1] + 2*phi[2] + phi[3])
print(Y)
print(X)

# sol = odeint(f, y0, X)
# def oden():
#     fi = lambda t, y: -(1 + t*y) / t**2
#     ODE = ode(fi)
#     ODE.set_integrator('dopri5')
#     ODE.set_initial_value(0, 0)
#     t = arange(a, b, N)
#     z = []
#     for i in arange(a, b, N):
#         ODE.integrate(i)
#         q = ODE.y
#         z.append(q[0])
#     return z, t
# sol2 = oden()
# print(sol2)

fig = plt.figure()
plt.plot(X, Y, 'ro')
# plt.plot( sol2)
plt.show()
plt.close(fig)
