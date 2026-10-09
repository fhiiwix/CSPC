"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('titration.csv', delimiter=',', skiprows=1)
V = data[:, 0]
pH = data[:, 1]


slope = np.gradient(pH, V)


idx_max = np.argmax(slope)
equiv_volume = V[idx_max]
equiv_pH = pH[idx_max]

print(f"Equivalence point volume: {equiv_volume:.2f} mL (pH = {equiv_pH:.2f})")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))


ax1.plot(V, pH, color='blue', label='pH curve')
ax1.axvline(equiv_volume, color='red', linestyle='--', label=f'Equiv point ({equiv_volume:.1f} mL)')
ax1.set_xlabel('Volume of Base (mL)')
ax1.set_ylabel('pH')
ax1.set_title('Titration Curve')
ax1.grid(True)
ax1.legend()


ax2.plot(V, slope, color='green', label='dpH / dV')
ax2.axhline(slope[idx_max], color='red', linestyle=':', label=f'Max slope = {slope[idx_max]:.2f}')
ax2.axvline(equiv_volume, color='red', linestyle='--')
ax2.set_xlabel('Volume of Base (mL)')
ax2.set_ylabel('Slope (dpH / dV)')
ax2.set_title('First Derivative (Slope)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig('titration.png')
plt.show()