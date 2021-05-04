from libHBCurveCalculator import *
import matplotlib.pyplot as plt

# Circuit parameters
lg = 2e-3
x = y = 0.2
x1 = y1 = p = 50e-3
FA = 0.95
N = 500

# Fundamental constants
pi = 3.141592654
mu0 = pi*4e-7

# Problem parameter
I = 10

# Geometric derivations
lm = 2*y + 2*x - 2*x1 - 2*y1 - lg
Am = FA*x1*p

Ag = (x1 + lg)*(p + lg)

# Magnetism derivations
F = I*N 


# Line
def getBm(Hm):
    return (Ag/Am)*mu0*(F-Hm*lm)/lg

def getIntersection(x_vector, y_one, y_two):
    i = np.abs(y_one - y_two).argmin()
    return x_vector[i], y_one[i]

# Curve
H_col, B_col = getData('iron_malleable.txt')

x_values = np.arange(0,20000,0.1)
y_line = getBm(x_values)
y_curve = np.array([calcB(x, H_col, B_col, strategy=1) for x in x_values])

Hm, Bm = getIntersection(x_values, y_line, y_curve)

# plt.plot(H_col, B_col)
plt.plot(x_values, y_line)
plt.plot(x_values, y_curve)
plt.plot(Hm, Bm, 'o')
plt.text(Hm, Bm+0.15, f'$H_m = {Hm}\,Av/m$\n$B_m = {Bm:.3f}\,Wb/m^2$',
         bbox = dict(boxstyle='square,pad=0.1',alpha=0.8,fc='white',ec='white'))
plt.axis([0,8000,0,3])
plt.legend(['Recta de carga','Curva de magentización'])
plt.xlabel('$H_m\,[Av/m]$')
plt.ylabel('$B_m\,[Wb/m^2]$')
plt.grid(True)
plt.show()

print(f'''Summary:
lg = {lg}
x = y = {x}
x1 = y1 = p = {x1}
FA = {FA}
N = {N}
I = {I}
lm = {lm}
Am = {Am}
Ag = {Ag}
F = {F}
''')
