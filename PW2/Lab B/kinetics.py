"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
t_data = data[:, 0]
C_data = data[:, 1]

C0 = C_data[0]

def total_error(k):
    C_model = C0 * np.exp(-k * t_data)
    return np.sum((C_data - C_model)**2)

res = minimize(total_error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
k_fitted = res.x[0]

print(f"Fitted rate constant k = {k_fitted:.4f}")

plt.figure(figsize=(7, 5))
plt.scatter(t_data, C_data, color='red', label='Measured data')

t_curve = np.linspace(min(t_data), max(t_data), 100)
C_curve = C0 * np.exp(-k_fitted * t_curve)
plt.plot(t_curve, C_curve, color='blue', label=f'Fit: C(t) = {C0:.2f}*exp(-{k_fitted:.2f}*t)')

plt.xlabel('Time (s)')
plt.ylabel('Concentration')
plt.title('First-Order Reaction Kinetics')
plt.legend()
plt.grid(True)
plt.savefig('kinetics.png')
plt.show()
