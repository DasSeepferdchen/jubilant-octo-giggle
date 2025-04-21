import numpy as np
spikes = np.random.rand(3, 3) * 0.1  # Fuzzy SNN-Simulation
time = np.linspace(0, 1, 3)  # Zeitdynamik
matrix = spikes * np.sin(time)  # Zacken-Muster
print(matrix)