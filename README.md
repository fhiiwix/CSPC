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