"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

#TODO 1
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

#TODO 2
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {a.mean():.2f} m/s^2")
print(f"Std of acceleration: {a.std():.2f} m/s^2")

#TODO 3
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y_rec - y))
print(f"Max reconstruction error: {max_diff:.4f} m")

#TODO 4
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 8))

ax1.plot(t, y, label='Position (y)', color='blue')
ax1.set_ylabel('Position (m)')
ax1.grid(True)

ax2.plot(t, v, label='Velocity (v)', color='orange')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)

ax3.plot(t, a, label='Acceleration (a)', color='red', alpha=0.6)
ax3.axhline(-9.81, color='black', linestyle='--', label='g = -9.81 m/s²')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.set_xlabel('Time (s)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig('motion.png')
plt.show()