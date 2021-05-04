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
    Hg = (F-Hm*lm)/lg
    Bg = mu0*Hg
    return (Ag/Am)*Bg

def getIntersection(x_vector, y_one, y_two):
    i = np.abs(y_one - y_two).argmin()
    return x_vector[i], y_one[i]

# Curve
H_col, B_col = getData('iron_malleable.txt')

x_values = np.arange(0,20000,0.1)
y_line = getBm(x_values)
y_curve = np.array([calcB(x, H_col, B_col, strategy=0) for x in x_values])

Hm, Bm = getIntersection(x_values, y_line, y_curve)

Hg = (F-Hm*lm)/lg
Bg = mu0*Hg
phi = Bm*Am
phi2 = Bg*Ag

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
Hm = {Hm}
Bm = {Bm}
Hg = {Hg}
Bg = {Bg}
phi = {phi}
phi2 = {phi2}
''')


plt.plot(x_values, y_line)
plt.plot(x_values, y_curve)
plt.plot(H_col, B_col, 'og')
plt.plot(Hm, Bm, 'ok')
plt.text(Hm, Bm+0.15, f'$H_m = {Hm}\,Av/m$\n$B_m = {Bm:.3f}\,Wb/m^2$',
         bbox = dict(boxstyle='square,pad=0.1',alpha=0.8,fc='white',ec='white'))
plt.axis([0,10000,0,2.5])
plt.legend(['Recta de carga','Curva de magentización'])
plt.xlabel('$H_m\,[Av/m]$')
plt.ylabel('$B_m\,[Wb/m^2]$')
plt.grid(True)
plt.show()
