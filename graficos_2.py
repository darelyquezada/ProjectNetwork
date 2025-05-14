import numpy as np
import matplotlib.pyplot as plt

signal = "111100010"
X = []
Y = []

# NRZ-L: 1 → low (0), 0 → high (1)
levels = [1 if bit == '1' else 0 for bit in signal]

# Create step points (tipo step)
for i, level in enumerate(levels):
    X.extend([i, i + 1])
    Y.extend([level, level])

plt.figure(figsize=(8, 3))
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

#Bipolar AMI

# Initialize variables
levels = []
X = []
Y = []

# Bipolar AMI Logic: 0 → no transition, 1 → alternate from +1 to -1
last_non_zero = -1  # Start with -1

for bit in signal:
    if bit == "1":
        last_non_zero *= -1  # Alternate between +1 and -1
        levels.append(last_non_zero)
    else:
        levels.append(0)  # No voltage for "0"

# Create step points (transitions exactly at the integer point)
for i, level in enumerate(levels):
    X.extend([i, i + 1])
    Y.extend([level, level])

# Plot configuration
plt.figure(figsize=(8, 3))
plt.step(X, Y, where='post')
plt.ylim(-1.5, 1.5)
plt.title("Signal Bipolar AMI")
plt.xlabel("Time")
plt.ylabel("Voltage Level")
plt.grid(True)

# Add bit labels
for idx, bit in enumerate(signal):
    plt.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)
plt.show()

#Pseudoternario

# Initialize variables
levels = []
X = []
Y = []
current_level = 0

# Pseudoternario Logic: 1 → no transition (0), 0 → alternate from +1 to -1
last_non_zero = -1  # Start with -1

for bit in signal:
    if bit == "0":
        last_non_zero *= -1  # Alternate between +1 and -1
        levels.append(last_non_zero)
    else:   # bit == "1"
        levels.append(0)  # No voltage for "1"

# Create step points (transitions exactly at the integer point)
for i, level in enumerate(levels):
    X.extend([i, i + 1])
    Y.extend([level, level])

# Plot configuration
plt.figure(figsize=(8, 3))
plt.step(X, Y, where='post')
plt.ylim(-0.5, 1.5)
plt.title("Signal Pseudoternario")
plt.xlabel("Time")
plt.ylabel("Voltage Level")
plt.grid(True)

# Add bit labels
for idx, bit in enumerate(signal):
    plt.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)
plt.show()

#Manchester

# Initialize variables
levels = []
X = []
Y = []
current_level = 0

# Manchester Logic: 1 → from low to high, 0 → from high to low

for bit in signal:
    if bit == "0":
        levels.append([1, 0]) # 1 -> 0
    else:   # bit == "1"
        levels.append([0, 1]) # 0 -> 1
        

# Create step points
for i, level in enumerate(levels):
    X.extend([i / 2, (i + 1) / 2])
    Y.extend([level, level])

# Plot configuration
plt.figure(figsize=(8, 3))
plt.step(X, Y, where='post')
plt.ylim(-0.5, 1.5)
plt.title("Signal Manchester")
plt.xlabel("Time")
plt.ylabel("Voltage Level")
plt.grid(True)

# Add bit labels at the center of each bit period
for idx, bit in enumerate(signal):
    plt.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)

plt.show()

# Código Diferencial

