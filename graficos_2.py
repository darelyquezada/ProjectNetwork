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
X = []
Y = []

# Codificación Manchester:
# 0 → Alto a Bajo (1 → 0)
# 1 → Bajo a Alto (0 → 1)

for i, bit in enumerate(signal):
    t0 = i          # inicio del bit
    t_half = i + 0.5  # mitad del bit (transición)
    t1 = i + 1      # fin del bit

    if bit == "0":
        # Bit 0 → Alto (1) a Bajo (0)
        X.extend([t0, t_half, t_half, t1])
        Y.extend([1, 1, 0, 0])
    else:
        # Bit 1 → Bajo (0) a Alto (1)
        X.extend([t0, t_half, t_half, t1])
        Y.extend([0, 0, 1, 1])

# Graficar
plt.figure(figsize=(10, 3))
plt.step(X, Y, where='post', linewidth=2, color='blue')
plt.ylim(-0.5, 1.5)
plt.yticks([0, 1], ['Bajo', 'Alto'])
plt.xticks(range(len(signal) + 1))
plt.grid(True)
plt.xlabel("Tiempo")
plt.ylabel("Nivel de voltaje")
plt.title("Codificación Manchester")

# Mostrar los bits encima del gráfico
for i, bit in enumerate(signal):
    plt.text(i + 0.5, 1.2, bit, ha='center', va='center', fontsize=10)

plt.tight_layout()
plt.show()
# Código Diferencial

signal_2 = "0100110011"
X = []
Y = []

# Nivel inicial como en la imagen: empieza en 1
current_level = 1

for i, bit in enumerate(signal_2):
    t_start = i
    t_mid = i + 0.5
    t_end = i + 1

    if bit == "0":
        # Transición al inicio
        current_level = 1 - current_level
        X.extend([t_start, t_mid])
        Y.extend([current_level, current_level])

        # Transición a la mitad
        current_level = 1 - current_level
        X.extend([t_mid, t_end])
        Y.extend([current_level, current_level])
    else:  # bit == "1"
        # Sin transición al inicio
        X.extend([t_start, t_mid])
        Y.extend([current_level, current_level])

        # Transición a la mitad
        current_level = 1 - current_level
        X.extend([t_mid, t_end])
        Y.extend([current_level, current_level])

# Graficar la señal
plt.figure(figsize=(10, 3))
plt.step(X, Y, where='post', linewidth=2, color='darkblue')
plt.ylim(-0.5, 1.5)
plt.yticks([0, 1], ['0', '1'])
plt.xticks(range(len(signal_2) + 1))
plt.grid(True)
plt.xlabel("Tiempo")
plt.ylabel("Nivel de voltaje")
plt.title("Codificación Diferencial (IEEE 802.5)")

# Etiquetar los bits
for i, bit in enumerate(signal_2):
    plt.text(i + 0.5, 1.3, bit, ha='center', va='center', fontsize=11)

plt.tight_layout()
plt.show()