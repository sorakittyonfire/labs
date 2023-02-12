import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
import sympy as sym

t = sym.Symbol('t')
y = sym.Function("y")(t)

diffeq = sym.Eq(y.diff(t), (y**2*t))
print(diffeq)
ics = {y.subs(t, 0): 1} 
ipv = sym.dsolve(diffeq, ics = ics) 
print(ipv)
ipv1 = ipv.rhs
ipv2 = ipv.rhs
func1 = sym.lambdify(t, ipv1,'numpy')
func2 = sym.lambdify(t, ipv2,'numpy')
t_ = np.linspace(-4, 0.99, 100)  
y1 = func1(t_)
y2 = func2(t_)
fig = plt.figure(figsize=(6,6))
plt.axvline(x=0, c="black", label="x=0")
ax1 = plt.subplot()
ax1.plot(t_,y1,color = "orange") 
ax1.plot(t_,y2,color = "orange") 
ax1.axvline(x=0, c="black", label="x=0") 
ax1.axhline(y=0, c="black", label="y=0") 
ax1.grid()
plt.show()  
