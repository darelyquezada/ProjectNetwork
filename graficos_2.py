import numpy as np
import matplotlib.pyplot as plt

señal = "111100010"
X = []
Y = []

# NRZ-L: 1 → bajo (0), 0 → alto (1)
niveles = [1 if bit == '1' else 0 for bit in señal]

# Crear los puntos escalonados (tipo step)
for i, nivel in enumerate(niveles):
    X.extend([i, i + 1])
    Y.extend([nivel, nivel])


plt.step(X, Y, where='post')
plt.ylim(-0.5, 1)
plt.title("Señal NRZ-L")
plt.xlabel("Tiempo")
plt.ylabel("Voltaje")
plt.grid(True)
plt.show()


#NRZ-I
#Bipolar  AMI
#Pseudoternario
#Manchester
#codigodiferenciaal