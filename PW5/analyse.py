import os
import numpy as np
import pandas as pd

def bandpass(x, fs, a=0.5, b=10.0):
    n = len(x)
    X = np.fft.fft(x)
    f = np.fft.fftfreq(n, d=1/fs)
    X[(np.abs(f) < a) | (np.abs(f) > b)] = 0
    return np.fft.ifft(X).real

def envelope(x, fs, win_s=0.5):
    w = int(round(win_s * fs))
    return np.convolve(np.abs(x), np.ones(w)/w, mode="same")

def analyse(csv_file):
    d = pd.read_csv(csv_file)
    t = d["time_s"].to_numpy()
    Z = d["Z"].to_numpy()
    N = d["N"].to_numpy()
    E = d["E"].to_numpy()
    fs = 1.0 / (t[1] - t[0])

    Z_clean = bandpass(Z, fs, a=0.5, b=10.0)
    N_clean = bandpass(N, fs, a=0.5, b=10.0)
    E_clean = bandpass(E, fs, a=0.5, b=10.0)

    H_clean = np.sqrt(N_clean**2 + E_clean**2)
    env_Z = envelope(Z_clean, fs, 0.5)
    env_H = envelope(H_clean, fs, 0.5)

    t_P = float(t[np.argmax(env_Z > 0.05 * np.max(env_Z))])
    env_H_after = np.where(t > (t_P + 2.0), env_H, 0.0)
    t_S = float(t[np.argmax(env_H_after > 0.10 * np.max(env_H))])

    vP, vS = 6.2, 3.6
    R = float((t_S - t_P) / (1.0 / vS - 1.0 / vP))

    H_raw = np.sqrt(N**2 + E**2)
    PGV = float(np.max(H_raw) * 100.0)
    M = float((np.log10(PGV) + np.log10(R) + 1.0) / 0.55)

    return {
        "event": os.path.basename(csv_file),
        "t_P": round(t_P, 2),
        "t_S": round(t_S, 2),
        "R_km": round(R, 2),
        "PGV_cm_s": round(PGV, 4),
        "M": round(M, 2)
    }

if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    rows = [
        analyse("data/seismogram_A.csv"),
        analyse("data/seismogram_B.csv")
    ]
    df_res = pd.DataFrame(rows)
    df_res.to_csv("results/events.csv", index=False)
    print(df_res.to_string(index=False))