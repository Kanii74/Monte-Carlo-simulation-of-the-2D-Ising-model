import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Lattice size (L x L grid)
L = 50

# Coupling strength (J > 0 → ferromagnetic)
J = 1.0

# Temperature (set to 0 to see pure ordering)
T = 0

# Random initial configuration of spins (+1 or -1)
spins = np.random.choice([-1, 1], size=(L, L))


def delta_energy(i, j):
    """
    Compute the energy change if we flip the spin at (i, j).
    Periodic boundary conditions are used.
    """
    s = spins[i, j]

    # Sum of the four nearest neighbours
    nn_sum = (
        spins[(i + 1) % L, j] +
        spins[(i - 1) % L, j] +
        spins[i, (j + 1) % L] +
        spins[i, (j - 1) % L]
    )

    # Energy difference from flipping s -> -s
    return 2 * J * s * nn_sum


def metropolis_step():
    """
    Perform one Monte Carlo sweep (L^2 attempted updates).
    """
    for _ in range(L * L):

        # Pick a random lattice site
        i = np.random.randint(0, L)
        j = np.random.randint(0, L)

        dE = delta_energy(i, j)

        # Metropolis acceptance rule
        if dE <= 0:
            spins[i, j] *= -1
        else:
            # Only matters if T > 0
            if T > 0 and np.random.rand() < np.exp(-dE / T):
                spins[i, j] *= -1

fig, ax = plt.subplots()
img = ax.imshow(spins, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_title(f"2D Ising Model (T = {T})")
ax.axis("off")

def update(frame):
    """
    Advance simulation and update image.
    """
    metropolis_step()
    img.set_array(spins)
    return [img]


animation = FuncAnimation(fig, update, frames=200, interval=50)

plt.show()


