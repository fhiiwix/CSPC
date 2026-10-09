"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x)
def k_imbalance(x):
    return ((2 * x)**2) / ((a - x) * (b - x)) - K

# TODO 2 (method 1): scipy.optimize.newton
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 (method 2): scipy.optimize.minimize on k_imbalance(x)**2
def objective(x):
    return k_imbalance(x[0])**2

res_slsqp = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium x (Newton): {x_newton:.4f}")
print(f"Equilibrium x (SLSQP):  {x_slsqp:.4f}")

# TODO 4: report equilibrium amounts and plot
nH2 = a - x_newton
nI2 = b - x_newton
nHI = 2 * x_newton

print(f"Equilibrium amounts: H2 = {nH2:.4f} mol, I2 = {nI2:.4f} mol, HI = {nHI:.4f} mol")

# Plotting
x_vals = np.linspace(0, 0.99, 200)
nH2_vals = a - x_vals
nI2_vals = b - x_vals
nHI_vals = 2 * x_vals

plt.figure(figsize=(7, 5))
plt.plot(x_vals, nH2_vals, label='H2 (mol)', color='blue')
plt.plot(x_vals, nI2_vals, label='I2 (mol)', color='green', linestyle='--')
plt.plot(x_vals, nHI_vals, label='HI (mol)', color='red')

plt.axvline(x_newton, color='black', linestyle=':', label=f'Equilibrium x = {x_newton:.2f}')

plt.xlabel('Extent of reaction (x)')
plt.ylabel('Amount (mol)')
plt.title('Chemical Equilibrium: H2 + I2 <=> 2 HI')
plt.legend()
plt.grid(True)
plt.savefig('equilibrium.png')
plt.show()