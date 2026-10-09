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