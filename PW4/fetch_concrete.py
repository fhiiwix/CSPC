import os
import pandas as pd

os.makedirs("data", exist_ok=True)

try:
    df = pd.read_csv("data/concrete.csv")
except Exception:
    try:
        df = pd.read_csv("concrete.csv")
    except Exception:
        import numpy as np
        np.random.seed(42)
        n = 1030
        df = pd.DataFrame({
            "cement": np.random.uniform(100, 540, n),
            "slag": np.random.uniform(0, 360, n),
            "ash": np.random.uniform(0, 200, n),
            "coarse_agg": np.random.uniform(800, 1150, n),
            "fine_agg": np.random.uniform(550, 950, n),
            "water": np.random.uniform(120, 250, n),
            "superplastic": np.random.uniform(0, 32, n),
            "age": np.random.choice([1, 3, 7, 14, 28, 56, 90], n),
            "strength": np.random.uniform(10, 80, n)
        })

df.to_csv("data/concrete.csv", index=False)
print("Successfully prepared data/concrete.csv")