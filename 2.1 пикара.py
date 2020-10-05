from sympy import symbols, integrate
import matplotlib.pyplot as plt

NN = 6
a = 1
b = 2
y0 = 1
x0 = a

def f(x_, y):
    return -(1 + x_*y) / x_**2

print(f(1, 2))

x = symbols('x')
N = 5
Y = [y0 for i in range(N)]
h = (b-a)/20
X = [a+i*h for i in range(20)]

for i in range(1, N):
    Y[i] = Y[0] + integrate(f(x, Y[i-1]), (x, a, x))
print(Y)

fig = plt.figure()
plt.plot(X, [Y[0]]*20)
for i in range(1, N):
    plt.plot(X, [Y[i].subs(x, X[j]) for j in range(20)])
plt.show()
print(X)
print([Y[N-1].subs(x, X[j]) for j in range(20)])

