# CSPC — Computer Science for Physics and Chemistry

## PW1 Lab A: Radioactive Decay Simulation & Testing

### Overview
This repository contains a Python implementation of a stochastic radioactive decay simulation. At each time step $\Delta t = 0.05$, atoms have an independent probability $P = \lambda \Delta t$ of decaying.

### Conda Environment
The project relies on a Conda environment `cspc` configured with Python 3.11, NumPy, and Pytest.

### Running Tests
To run the automated test suite for the decay module, activate the environment and execute `pytest`:

```bash
conda activate cspc
cd "PW1/Lab A"
pytest -v