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

- **Mean acceleration:** Measured average acceleration is `-8.58 m/s²` (close to $g = -9.81\text{ m/s}^2$, confirming free fall)[cite: 1, 5].
- **Noise observation:** Numerical differentiation (`np.gradient`) amplifies noise because small fluctuations in position measurements result in large changes in computed rates when divided by small time steps ($\Delta t$)[cite: 1, 2].
- **Integration result:** Integrating the noisy acceleration back up suppresses the noise due to cancellation during summation, recovering the original position within a maximum error of `0.7846 m`[cite: 2, 5].