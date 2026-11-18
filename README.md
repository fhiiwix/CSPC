# CSPC Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:
```bash```
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

## PW1 Lab A: Reproducible Foundations

**What I built:**
Set up the CSPC course repository, configured the Conda environment, implemented unit tests for radioactive decay simulation, and measured NumPy performance gains.

**Speed comparison (loop vs NumPy):**

    loop: 1.8302 s

    numpy: 0.0002 s

    speed-up: 11103.52x faster

**Tests: all passing? yes**

**Conclusion:**
NumPy vectorized operations provide a massive speed-up compared to standard Python loops for stochastic decay calculations. Configuring Pytest and Git ensures reproducibility and proper trackability across the development cycle.

## PW1 Lab B: Data, Plotting, and Automation

**What I built:**
Implemented `plot.py` to compare observed decay data against the theoretical analytical law, and automated the graph generation pipeline using Snakemake.

**Data & Plot Analysis:**
The observed data matches the analytical curve ($N_0 e^{-\lambda t}$) extremely well. The scatter points align closely with the exponential decay line, showing that the physical process follows theoretical predictions.

**Snakemake Pipeline:**
The Snakemake pipeline automates `figure.png` generation by monitoring file modification dates, ensuring the plot updates automatically when code or data changes while skipping unnecessary executions.

## PW2 Lab A: Motion from Tracking Data

- **Mean acceleration:** Measured average acceleration is `-8.58 m/s²` (close to $g = -9.81\text{ m/s}^2$, confirming free fall).
- **Noise observation:** Numerical differentiation (`np.gradient`) amplifies noise because small fluctuations in position measurements result in large changes in computed rates when divided by small time steps ($\Delta t$).
- **Integration result:** Integrating the noisy acceleration back up suppresses the noise due to cancellation during summation, recovering the original position within a maximum error of `0.7846 m`.

## PW2 Lab B: Optimization in Chemistry

- **Method Comparison (Part 2):**
  - On a simple convex function $f(x) = (x-3)^2 + 1$, all three methods (Gradient Descent, Newton's method, and SLSQP) easily converged to the global minimum at $x = 3.0000$.
  - On a non-convex function $g(x) = x^4 - 3x^2 + x + 5$, the starting point and algorithm mattered significantly:
    - From $x_0 = 0$: GD and SLSQP reached the local minimum at $x \approx -1.3008$, while Newton's method landed on a stationary point at $x \approx 0.1699$ (which is a local maximum, $g'' < 0$).
    - From $x_0 = 2$: GD and Newton converged to $x \approx 1.1309$ (local minimum), whereas SLSQP reached the deeper minimum at $x \approx -1.3006$.

- **Kinetics Fit (Part 3):**
  - Fitted reaction rate constant: $k = 0.2618\text{ s}^{-1}$.

- **Chemical Equilibrium (Part 4):**
  - Equilibrium extent $x = 0.6638$ (both Newton and SLSQP agreed).
  - Equilibrium composition: $n_{\text{H}_2} = 0.3362\text{ mol}$, $n_{\text{I}_2} = 0.3362\text{ mol}$, $n_{\text{HI}} = 1.3277\text{ mol}$.

- **Titration Equivalence Point (Part 5):**
  - Equivalence point volume: $50.00\text{ mL}$ (where $\text{pH} = 7.00$ and slope peaks at $4.00$).


# Practical Work 3: Data, Distributions, Testing, and Causation

**Author:** Sadigov Mahammad  
**Course:** Computer Science for Physics and Chemistry (CSPC) — UFAZ  

---

## Session 1: Characterising Heart Disease Data

### 1. Dataset Overview
The Cleveland Heart Disease dataset (`Heart_disease_cleveland_new.csv`) was loaded and inspected using `pandas`. Four continuous clinical variables were isolated for analysis: `age`, `chol` (serum cholesterol), `trestbps` (resting blood pressure), and `thalach` (maximum heart rate achieved).

### 2. Distribution Shapes & Normality Checks
Histograms (`heart_distributions.png`) and the **Shapiro-Wilk normality test** were used to evaluate each continuous variable:

* **`age`**: Approximately bell-shaped and symmetric around middle age, though slightly deviating from strict normality under Shapiro-Wilk.
* **`chol`**: Right-skewed with a long tail towards high cholesterol levels (non-normal).
* **`trestbps`**: Moderately right-skewed with clustering around standard/elevated resting blood pressure values (non-normal).
* **`thalach`**: Slightly left-skewed ($W = 0.9765, p = 0.0001$), deviating from strict Gaussian normality due to its tail towards lower heart rates.

---

## Session 2: Drawing Conclusions

### 3. Maximum Heart Rate Comparison (`thalach` by `target`)
* **Method:** Because the sample sizes are large enough for the Central Limit Theorem to apply and variances between groups may differ, **Welch's independent two-sample t-test** was applied to compare healthy patients (`target = 0`) against heart-disease patients (`target = 1`).
* **Result:** $t = 7.8579$, $p = 9.11 \times 10^{-14}$.
* **Conclusion:** There is a highly statistically significant difference between the two groups. Healthy patients reach a substantially higher maximum heart rate on average than patients with heart disease, which is clearly confirmed by the non-overlapping 95% confidence intervals in `thalach_comparison.png`.

### 4. Age vs. Maximum Heart Rate (`age` vs. `thalach`)
* **Method:** Pearson correlation coefficient ($r$) and scatter plot (`age_thalach_scatter.png`).
* **Result:** $r = -0.3938$, $p = 1.11 \times 10^{-12}$.
* **Conclusion:** Age and maximum heart rate exhibit a statistically significant, moderate negative linear relationship — as age increases, peak achievable heart rate decreases.

---

## Dataset 2: Chemical-Exposure Mystery (Correlation vs. Causation)

### 5. Naive Bivariate Analysis
Computing direct Pearson correlations between each chemical and `malignancy` across the full dataset (`chemicals_cancer.csv`) yielded:
* **Cadmium vs. Malignancy:** $r = 0.8800$ (very strong positive correlation)
* **Benzene vs. Malignancy:** $r = 0.3847$ (weak-to-moderate correlation)

**Naive Verdict:** Taken at face value, **Cadmium** appears to be the primary driver of tumour malignancy.

### 6. Accounting for Confounding Variables
Checking relationships with environmental background (`pollution_index`) revealed a classic confounding structure:
* **Cadmium vs. Pollution Index:** $r = 0.9819$
* **Malignancy vs. Pollution Index:** $r = 0.8951$
* **Benzene vs. Pollution Index:** $r = 0.0545$

To isolate the true chemical effect, the dataset was stratified to patients living within a narrow pollution band ($45 < \text{pollution\_index} < 55$):
* **Stratified Cadmium vs. Malignancy:** $r = -0.0400$ (drops to zero)
* **Stratified Benzene vs. Malignancy:** $r = 0.6579$ (emerges strongly)

**Final Conclusion:** **Benzene** is the true causal driver of tumour malignancy. **Cadmium** only appeared guilty in the naive analysis because both cadmium exposure and cancer malignancy independently rise with the regional `pollution_index`. Once pollution is held constant, cadmium's effect vanishes completely while benzene's direct toxic effect becomes clear.

---

## Bonus: Category Unpredictability
Using normalized value counts on the `target` column, the **Shannon Entropy** was calculated as:
$$H = -\sum p_i \log_2(p_i) = 0.9951 \text{ bits}$$
Since the maximum possible entropy for a binary variable is $1.0$ bit, the dataset is nearly evenly balanced (~50/50 split), meaning blind guessing offers almost no advantage over random chance.

## Practical Work 4: Machine Learning: Supervised and Unsupervised

### Session A: Concrete Compressive Strength (Supervised)
* **Data Cleaning:** Removed 25 duplicate rows from 1030 initial laboratory samples to prevent data leakage between train/test splits[cite: 11].
* **Linear Regression:** Fitted on 8 ingredients/features. Residual plots against age (`results/residuals_age.png`) show a systematic non-linear pattern, confirming that age affects strength logarithmically rather than linearly.
* **Polynomial Regression:** Tested degrees 1 to 4. Degree 2/3 significantly improves $R^2$, while Degree 4 overfits catastrophically ($p = 494$ features vs. 824 training rows).
* **Classification (Threshold $\ge 40$ MPa):** Evaluated KNN ($K=5$) and Decision Trees. KNN achieved strong test accuracy (~95.6%), balancing precision and recall.

### Session B: Wine Chemistry (Unsupervised)
* **PCA & Scaling:** Comparing raw vs. scaled PCA demonstrates that unscaled features with large numerical ranges (like proline) completely dominate PC1. Scaling puts all 13 chemical measurements on an equal footing.
* **Scree Plot:** Approximately 3-4 components are needed to retain 90% of the total variance (`results/scree_plot.png`).
* **K-Means Clustering & Agreement:** Unsupervised K-Means ($k=3$) on scaled data achieved an exceptional agreement score (~90%+) when cross-tabulated against true grape cultivars (`results/B_agreement.csv`), proving that chemical composition naturally segregates the wine varieties without seeing labels.

### Snakemake Automation
* The entire workflow is fully automated via `Snakefile`. Running `snakemake --cores 1` reproduces all data fetching, model training, evaluations, and generates all required plots and CSV outputs in `results/`.

## Practical Work 5: Signal Processing: Where Was the Earthquake, and How Strong?

### 1. Waveform Inspection & Background Noise
* **Channels (`PW5/results/1_three_channels.png`):** The first, weaker shaking (P-wave, ~108 s) appears clearest on the vertical **Z** channel because P-waves are compressional waves arriving steeply from below. The later, much stronger shaking (S-wave, ~144 s) dominates the horizontal **N** and **E** channels due to transverse shear motion.
* **First 60 s (`PW5/results/1_zoom_60s.png`):** The station is not completely still before the earthquake; continuous low-amplitude oscillations (~0.005 mm/s) are present across all channels.

### 2. Frequency Spectrum (FFT)
* **Index vs. Frequency (`PW5/results/2a_fft_index_vs_freq.png`):** `np.fft.fftfreq` maps array indices to physical frequencies in Hz (from $-f_s/2$ to $+f_s/2$). Because the input seismogram is strictly real-valued, its Fourier transform is conjugate-symmetric ($X[-f] = X^*[f]$), making the amplitude spectrum mirrored around 0 Hz.
* **Microseism vs. Earthquake (`PW5/results/2b_loglog_spectrum.png`):** Background microseism noise peaks strongly between **0.1 and 0.4 Hz** (ocean wave energy). The earthquake adds most of its energy in the **0.5–10 Hz** band.

### 3. Inverse FFT & Band-Pass Filtering
* **Invertibility:** `np.allclose(np.fft.ifft(np.fft.fft(Z)).real, Z)` returns `True`. Frequency-domain filtering relies on this exact round-trip invertibility so that zeroing out unwanted frequency bins and applying `ifft` alters only the targeted noise frequencies without distorting the remaining signal.
* **Cut-offs (`0.5–10 Hz`) & Removed Signal (`PW5/results/3c_removed_noise.png`):** Cutting below 0.5 Hz removes the ocean microseism and long-period surface waves, while cutting above 10 Hz eliminates high-frequency sensor/ambient noise. Plotting `Z_raw - Z_clean` reveals the continuous background microseism plus large low-frequency surface waves arriving after the S-wave.

### 4. Envelope & Smoothing Window
* **Window Comparison (`PW5/results/4_envelope_windows.png`):** A **0.05 s** window is too short—individual oscillation cycles leak through, causing premature false triggers. A **5.0 s** window is too long—it smears the sharp wave onset backward in time, shifting the apparent arrival earlier and flattening peaks. **0.5 s** cleanly tracks the amplitude buildup without distorting onset timing.

### 5. Arrival Times & Epicentral Distance
* **Arrivals (`PW5/results/5_arrivals.png`):** For `seismogram_A.csv`, $t_P = 108.42\text{ s}$ and $t_S = 144.08\text{ s}$, whereas the horizontal envelope peak occurs later at $152.03\text{ s}$. Using the maximum instead of the onset would overestimate $t_S - t_P$ and yield a falsely large distance because peak energy arrives several seconds after the initial shear-wave front.
* **Distance & Origin Time:** With $v_P = 6.2\text{ km/s}$ and $v_S = 3.6\text{ km/s}$, $R = 306.13\text{ km}$. A $1\text{ s}$ uncertainty in $t_S$ shifts $R$ by $\pm 8.58\text{ km}$. The earthquake occurred at origin time $t_0 = t_P - R/v_P = 59.04\text{ s}$.

### 6. Spectrogram (`PW5/results/7_spectrogram.png`)
* The spectrogram resolves how frequency content evolves over time (which a single full-record FFT cannot show). The **P-wave** (~108 s) arrives with the highest frequencies (up to ~10 Hz), followed by the **S-wave** (~144 s) with intermediate frequencies, and finally the **surface waves** (>155 s) carrying the lowest frequencies (<1–2 Hz).

### 7. Magnitude Scale
* **Distance Correction ($\log_{10} R$):** Seismic waves attenuate as they spread outward. Without the $+\log_{10} R$ term, an identical earthquake recorded twice as far away would have a lower PGV and falsely appear smaller (by $\Delta M = \log_{10}(2)/0.55 \approx 0.55$ units).
* **Scaling Factor:** Increasing $M$ by 1 unit requires $\Delta \log_{10}(\text{PGV}) = 0.55$, meaning PGV increases by $10^{0.55} \approx 3.55$ times at the same distance.

### 8. Results Comparison (`PW5/results/events.csv`)

| Record | $t_P$ (s) | $t_S$ (s) | Distance $R$ (km) | PGV (cm/s) | Magnitude $M$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `seismogram_A.csv` | 108.42 | 144.08 | 306.13 | 1.5105 | 6.66 |
| `seismogram_B.csv` | 84.25 | 102.43 | 156.07 | 0.5711 | 5.36 |

* **Comparison:** **`seismogram_B.csv`** was closer ($156.07\text{ km}$ vs. $306.13\text{ km}$), while **`seismogram_A.csv`** was stronger ($M = 6.66$ vs. $M = 5.36$).

### 9. Snakemake Workflow
* **Reproducing PW5:** `snakemake --cores 1`
* **Behavior:**
  * Running `snakemake --cores 1` after deleting `results/` executes `analyse` followed by `report`.
  * Running it a second time immediately reports `Nothing to be done (all requested files are present and up to date)` because output timestamps are newer than all inputs.
  * Modifying only `report.py` reruns only `report`, skipping `analyse` since `results/events.csv` is still up to date.
  * Modifying `analyse.py` reruns both `analyse` and downstream `report` because `events.csv` is regenerated and becomes newer than `report.txt`.