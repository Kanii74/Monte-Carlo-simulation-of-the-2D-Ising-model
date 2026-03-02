# Monte Carlo Simulation of the 2D Ising Model

This project implements a simple 2D Ising model using the Metropolis Monte Carlo algorithm in Python.  
It simulates how spins on a square lattice evolve over time due to nearest-neighbour interactions.

---

## Overview

The Ising model is a standard model in statistical mechanics used to study magnetism and phase transitions.

In this implementation:

- A square lattice of size `L × L` is created.
- Each lattice site contains a spin with value `+1` or `-1`.
- Spins interact only with their four nearest neighbours.
- Periodic boundary conditions are used.
- The system evolves using the Metropolis acceptance rule.

---

## Physical Model

Each spin interacts with its neighbours through the Hamiltonian:

H = -J ∑⟨i,j⟩ sᵢ sⱼ

where:

- `sᵢ = ±1`
- `J` is the coupling strength
- The sum runs over nearest-neighbour pairs

For `J > 0`, the system is ferromagnetic, meaning aligned spins are energetically favourable.

---

## Algorithm

The simulation uses the Metropolis Monte Carlo method:

1. Select a random lattice site `(i, j)`.
2. Compute the energy change ΔE if the spin is flipped.
3. Apply the acceptance rule:
   - If ΔE ≤ 0 → accept the flip.
   - If ΔE > 0 → accept with probability exp(-ΔE / T).

One full Monte Carlo sweep consists of `L²` attempted spin updates.

---

## Parameters

Inside the script, you can modify:

```python
L = 50      # Lattice size
J = 1.0     # Coupling strength
T = 0       # Temperature
