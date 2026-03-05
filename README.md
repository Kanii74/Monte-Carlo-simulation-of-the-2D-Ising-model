# Monte Carlo Simulation of the 2D Ising Model

This project implements a simple **2D Ising model** using the **Metropolis Monte Carlo algorithm** in Python.
It simulates how spins on a square lattice evolve over time due to **nearest-neighbour interactions**, illustrating how local interactions can produce large-scale magnetic ordering.

The simulation provides a visual representation of how **magnetic domains emerge and evolve** as the system approaches equilibrium. Such simulations are widely used in **computational statistical mechanics** to study collective behavior in many-body systems.

---

## Overview

The **Ising model** is one of the most fundamental models in **statistical mechanics** used to study **magnetism, phase transitions, and critical phenomena**.

Originally introduced to describe **ferromagnetic materials**, the model captures how microscopic interactions between atomic spins can produce **macroscopic magnetic behavior**.

In this implementation:

* A square lattice of size `L × L` is created.
* Each lattice site contains a spin with value `+1` or `-1`.
* Spins interact only with their four nearest neighbours.
* Periodic boundary conditions are used.
* The system evolves using the **Metropolis acceptance rule**.

Periodic boundary conditions effectively remove edge effects by making the lattice behave like a **toroidal surface**, ensuring that every spin has exactly four neighbours.

The system evolves stochastically through Monte Carlo updates, allowing the lattice to relax toward **low-energy configurations** that minimize the total Hamiltonian.

---

## Physical Model

Each spin interacts with its neighbours through the Hamiltonian

$$
H = -J \sum_{\langle i,j \rangle} s_i s_j
$$

where

* $s_i = \pm 1$ represents the spin at lattice site $i$
* $J$ is the coupling strength between neighbouring spins
* The sum runs over all **nearest-neighbour spin pairs**

This Hamiltonian measures the **total interaction energy** of the spin configuration.

When neighboring spins are aligned ($s_i s_j = +1$), the contribution to the energy is negative and therefore energetically favorable.
When spins are anti-aligned ($s_i s_j = -1$), the contribution increases the energy.

This Hamiltonian favors **aligned spins** when $J > 0$, corresponding to a **ferromagnetic system**.

Key physical properties:

* When neighboring spins align ($s_i s_j = +1$), the energy decreases.
* When neighboring spins are anti-aligned ($s_i s_j = -1$), the energy increases.

As a result, the system naturally tends to form **clusters or domains of aligned spins** that reduce the total energy.

At finite temperature, thermal fluctuations compete with this ordering tendency. This competition leads to a **phase transition** between an ordered and disordered state.

For the **2D square lattice Ising model**, the exact critical temperature is

$$
T_c = \frac{2J}{\ln(1+\sqrt{2})}
$$

Below this temperature the system becomes **magnetically ordered**, meaning most spins align in the same direction.

Above the critical temperature the system enters a **paramagnetic phase**, where thermal fluctuations dominate and long-range magnetic order disappears.

---

## Algorithm

The simulation uses the **Metropolis Monte Carlo method**, a widely used technique for sampling configurations according to the **Boltzmann distribution**.

The probability of a configuration with energy $E$ occurring at temperature $T$ is proportional to

$$
P(E) \propto e^{-E/T}
$$

The Metropolis algorithm allows us to generate configurations with this probability distribution.

At each step:

1. Select a random lattice site $(i, j)$.
2. Compute the energy change $\Delta E$ if the spin is flipped.
3. Apply the acceptance rule:

* If $\Delta E \le 0$ → accept the flip.
* If $\Delta E > 0$ → accept with probability

$$
P = \exp\left(-\frac{\Delta E}{T}\right)
$$

This rule ensures that moves lowering the energy are always accepted, while moves that increase the energy are sometimes accepted due to **thermal fluctuations**.

Allowing these occasional uphill moves prevents the system from becoming trapped in **local energy minima** and ensures proper sampling of the equilibrium distribution.

One full Monte Carlo sweep consists of $L^2$ attempted spin updates.

This means that, on average, every lattice site is updated once per sweep.

In the animation produced by the simulation, each frame corresponds approximately to **one Monte Carlo sweep**, illustrating how the system evolves toward equilibrium.

---

## Parameters

Inside the script, you can modify:

```python
L = 50      # Lattice size
J = 1.0     # Coupling strength
T = 0       # Temperature
```

Parameter meanings:

* `L` controls the **size of the lattice**
* `J` determines the **interaction strength between spins**
* `T` represents the **temperature**, which controls thermal fluctuations

Increasing the lattice size allows the simulation to better approximate the **thermodynamic limit**, where the number of particles becomes very large.

Temperature plays a central role in determining the system’s behavior:

* **Low temperature** → ordered magnetic domains form
* **Intermediate temperature** → competing order and fluctuations
* **High temperature** → disordered paramagnetic phase

---

## Simulation Results

The following figures illustrate how the spin lattice evolves under different physical parameters.

The plots show the lattice configuration where

* **Red** represents spin $+1$
* **Blue** represents spin $-1$

As the simulation progresses, spins reorganize into **energetically favorable configurations**, forming **magnetic domains**.

This process is known as **domain coarsening**, where small clusters merge into larger regions of aligned spins over Monte Carlo time.

---

### Case 1 — Zero Temperature Ordering

Parameters: `L = 50`, `J = 1.0`, `T = 0`

At zero temperature the system only accepts moves that **lower the energy**.

Thermal fluctuations are absent, so the system behaves like a **pure energy minimization process**.

Small clusters of aligned spins quickly grow and merge into **large magnetic domains**, eventually approaching a nearly fully ordered state.

![ising\_simulation](https://github.com/user-attachments/assets/ae0d085e-cba4-4888-9eb6-b2bff0220624)

---

### Case 2 — Finite Temperature Fluctuations

Parameters: `L = 50`, `J = 1.0`, `T = 1.5`

At finite temperature, **thermal fluctuations** allow energetically unfavorable spin flips with probability

$$
P = \exp\left(-\frac{\Delta E}{T}\right)
$$

This produces a dynamic competition between **energy minimization and thermal disorder**.

Domains still form, but their boundaries fluctuate due to the presence of thermal excitations.

![ising\_simulation](https://github.com/user-attachments/assets/e202fae2-ccbf-4dbf-bcdb-4c665ce32ad7)

---

### Case 3 — High Temperature Disorder

Parameters: `L = 50`, `J = 1.0`, `T = 3.0`

At temperatures above the critical temperature $T_c$, the system becomes **paramagnetic**.

Thermal fluctuations dominate over interaction energy, preventing long-range ordering.

Spins flip frequently and the lattice remains in a **highly disordered state** with only short-lived clusters.

![ising\_simulation\_](https://github.com/user-attachments/assets/c5469a0f-53eb-49ac-b54a-3f1e01c1fbe6)

---

### Case 4 — Larger Lattice

Parameters: `L = 100`, `J = 1.0`, `T = 0`

Increasing the lattice size allows the formation of **larger magnetic domains** and provides a better approximation to the **thermodynamic limit**.

Larger systems display richer domain structures and slower coarsening dynamics.

![ising\_simulation\_3](https://github.com/user-attachments/assets/6dd24576-b09e-48eb-9b6a-2404e1aea7af)
