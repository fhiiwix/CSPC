"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize


def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

print("=== Part 2A: Convex function f(x) = (x-3)^2 + 1 ===")

x_gd = 0.0
alpha = 0.1
for _ in range(100):
    x_gd = x_gd - alpha * df(x_gd) 
print(f"Gradient Descent: x = {x_gd:.4f}")


x_newt = newton(df, x0=0, fprime=d2f) 
print(f"Newton method:     x = {x_newt:.4f}")


res_slsqp = minimize(f, x0=0, method="SLSQP")
print(f"SLSQP minimize:    x = {res_slsqp.x[0]:.4f}\n")


def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

print("=== Part 2B: Non-convex function g(x) = x^4 - 3x^2 + x + 5 ===")

for x0 in [0, 2]:
    print(f"--- Starting from x0 = {x0} ---")
    
    
    x_gd = float(x0)
    for _ in range(200):
        x_gd = x_gd - 0.01 * dg(x_gd)
    print(f"Gradient Descent: x = {x_gd:.4f}")

    
    try:
        x_newt = newton(dg, x0=x0, fprime=d2g)
        curv = d2g(x_newt)
        kind = "minimum" if curv > 0 else "maximum"
        print(f"Newton:           x = {x_newt:.4f} (d2g = {curv:.2f} -> {kind})")
    except Exception as e:
        print(f"Newton failed: {e}")

  
    res = minimize(g, x0=x0, method="SLSQP")
    print(f"SLSQP:            x = {res.x[0]:.4f}\n")
