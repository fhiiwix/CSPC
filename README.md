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