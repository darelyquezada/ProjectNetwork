import numpy as np
import matplotlib.pyplot as plt

signal = "111100010"
X = []
Y = []

# NRZ-L: 1 → bajo (0), 0 → alto (1)
levels = [1 if bit == '1' else 0 for bit in signal]

# Crear los puntos escalonados (tipo step)
for i, level in enumerate(levels):
    X.extend([i, i + 1])
    Y.extend([level, level])


plt.step(X, Y, where='post')
plt.ylim(-0.5, 1)
plt.title("Signal NRZ-L")
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.grid(True)
plt.show()

#NRZ-I

# Initialize variables
levels = []
X = []
Y = []
current_level = 0

# NRZ-I Logic: 1 → transition, 0 → no transition
for bit in signal:
    if bit == "1":
        current_level = 1 - current_level  # Toggle level
    levels.append(current_level)

# Create step points (transitions exactly at the integer point)
for i, level in enumerate(levels):
    X.extend([i, i + 1])
    Y.extend([level, level])

# Plot configuration
plt.figure(figsize=(8, 3))
plt.step(X, Y, where='post')
plt.ylim(-0.5, 1.5)
plt.title("Signal NRZ-I")
plt.xlabel("Time")
plt.ylabel("Voltage Level")
plt.grid(True)

# Add bit labels
for idx, bit in enumerate(signal):
    plt.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)

plt.show()

#Bipolar  AMI
#Pseudoternario
#Manchester
#codigodiferenciaal