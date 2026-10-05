import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

# Замер времени для чистого Python (loop)
t0 = time.perf_counter()
simulate_loop(N0, lam)
t_loop = time.perf_counter() - t0

# Замер времени для NumPy версии
t0 = time.perf_counter()
simulate(N0, lam)
t_numpy = time.perf_counter() - t0

speedup = t_loop / t_numpy

print(f"Pure Python loop: {t_loop:.4f} s")
print(f"NumPy vectorised: {t_numpy:.4f} s")
print(f"Speed-up factor:  {speedup:.2f}x faster")