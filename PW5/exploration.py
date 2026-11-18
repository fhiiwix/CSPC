import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

os.makedirs("results", exist_ok=True)

d = pd.read_csv("data/seismogram_A.csv")
t = d["time_s"].to_numpy()
Z = d["Z"].to_numpy()
N = d["N"].to_numpy()
E = d["E"].to_numpy()
fs = 1.0 / (t[1] - t[0])

fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
axes[0].plot(t, Z * 1000, lw=0.6)
axes[0].set_ylabel("Z (mm/s)")
axes[0].set_title("Seismogram A: Three Channels")
axes[1].plot(t, N * 1000, lw=0.6)
axes[1].set_ylabel("N (mm/s)")
axes[2].plot(t, E * 1000, lw=0.6)
axes[2].set_ylabel("E (mm/s)")
axes[2].set_xlabel("Time (s)")
plt.tight_layout()
plt.savefig("results/1_three_channels.png", dpi=200)
plt.close()

mask60 = t <= 60
fig, axes = plt.subplots(3, 1, figsize=(10, 6), sharex=True)
axes[0].plot(t[mask60], Z[mask60] * 1000, lw=0.7)
axes[0].set_ylabel("Z (mm/s)")
axes[0].set_title("Seismogram A: First 60 s (Background Microseism)")
axes[1].plot(t[mask60], N[mask60] * 1000, lw=0.7)
axes[1].set_ylabel("N (mm/s)")
axes[2].plot(t[mask60], E[mask60] * 1000, lw=0.7)
axes[2].set_ylabel("E (mm/s)")
axes[2].set_xlabel("Time (s)")
plt.tight_layout()
plt.savefig("results/1_zoom_60s.png", dpi=200)
plt.close()

N_samples = len(Z)
X_fft = np.fft.fft(Z)
freqs = np.fft.fftfreq(N_samples, d=1/fs)
amp = np.abs(X_fft) / N_samples * 2

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
axes[0].plot(amp, lw=0.7)
axes[0].set_title("FFT Amplitude vs Array Index")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Amplitude (m/s)")
axes[1].plot(freqs, amp, lw=0.7)
axes[1].set_title("FFT Amplitude vs Frequency (Hz)")
axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Amplitude (m/s)")
plt.tight_layout()
plt.savefig("results/2a_fft_index_vs_freq.png", dpi=200)
plt.close()

Z_quiet = Z[mask60]
Nq = len(Z_quiet)
fq = np.fft.fftfreq(Nq, d=1/fs)
amp_q = np.abs(np.fft.fft(Z_quiet)) / Nq * 2

plt.figure(figsize=(8, 5))
plt.loglog(freqs[freqs > 0], amp[freqs > 0], label="Whole record", alpha=0.8, lw=0.8)
plt.loglog(fq[fq > 0], amp_q[fq > 0], label="First 60s (Quiet noise)", alpha=0.8, lw=0.9)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (m/s)")
plt.title("Amplitude Spectrum (Log-Log)")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.savefig("results/2b_loglog_spectrum.png", dpi=200)
plt.close()

def bandpass(x, fs, a=0.5, b=10.0):
    n = len(x)
    X = np.fft.fft(x)
    f = np.fft.fftfreq(n, d=1/fs)
    X[(np.abs(f) < a) | (np.abs(f) > b)] = 0
    return np.fft.ifft(X).real

Z_clean = bandpass(Z, fs, 0.5, 10.0)
N_clean = bandpass(N, fs, 0.5, 10.0)
E_clean = bandpass(E, fs, 0.5, 10.0)

plt.figure(figsize=(10, 4))
plt.plot(t, (Z - Z_clean) * 1000, color="gray", lw=0.7)
plt.title("Removed Signal (Z_raw - Z_clean) in mm/s")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (mm/s)")
plt.tight_layout()
plt.savefig("results/3c_removed_noise.png", dpi=200)
plt.close()

def get_envelope(x, fs, win_s):
    w = int(round(win_s * fs))
    return np.convolve(np.abs(x), np.ones(w)/w, mode="same")

env_Z_005 = get_envelope(Z_clean, fs, 0.05)
env_Z_05 = get_envelope(Z_clean, fs, 0.5)
env_Z_5 = get_envelope(Z_clean, fs, 5.0)

plt.figure(figsize=(10, 4.5))
plt.plot(t, env_Z_005 * 1000, label="Window = 0.05 s", alpha=0.6, lw=0.6)
plt.plot(t, env_Z_05 * 1000, label="Window = 0.5 s", color="black", lw=1.2)
plt.plot(t, env_Z_5 * 1000, label="Window = 5.0 s", color="red", lw=1.5)
plt.xlim(40, 140)
plt.xlabel("Time (s)")
plt.ylabel("Envelope (mm/s)")
plt.title("Effect of Window Width on Z Envelope")
plt.legend()
plt.tight_layout()
plt.savefig("results/4_envelope_windows.png", dpi=200)
plt.close()

H_clean = np.sqrt(N_clean**2 + E_clean**2)
env_H_05 = get_envelope(H_clean, fs, 0.5)

t_P = t[np.argmax(env_Z_05 > 0.05 * np.max(env_Z_05))]
env_H_after = np.where(t > (t_P + 2.0), env_H_05, 0)
t_S = t[np.argmax(env_H_after > 0.10 * np.max(env_H_05))]

fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
for ax, sig, name in zip(axes, [Z_clean, N_clean, E_clean], ["Z filtered (mm/s)", "N filtered (mm/s)", "E filtered (mm/s)"]):
    ax.plot(t, sig * 1000, lw=0.6)
    ax.axvline(t_P, color="green", ls="--", lw=1.5, label=f"t_P = {t_P:.2f}s")
    ax.axvline(t_S, color="red", ls="--", lw=1.5, label=f"t_S = {t_S:.2f}s")
    ax.set_ylabel(name)
    ax.legend(loc="upper right")
axes[2].set_xlabel("Time (s)")
axes[0].set_title("Filtered Waveforms with P- and S-Wave Arrivals")
plt.tight_layout()
plt.savefig("results/5_arrivals.png", dpi=200)
plt.close()

f_spec, t_spec, Sxx = signal.spectrogram(Z, fs=fs, nperseg=256)
plt.figure(figsize=(10, 4.5))
plt.pcolormesh(t_spec, f_spec, 10 * np.log10(Sxx + 1e-24), shading="gouraud", cmap="inferno")
plt.ylim(0, 10)
plt.colorbar(label="Power/Frequency (dB/Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Spectrogram of Raw Z Channel (0-10 Hz)")
plt.tight_layout()
plt.savefig("results/7_spectrogram.png", dpi=200)
plt.close()