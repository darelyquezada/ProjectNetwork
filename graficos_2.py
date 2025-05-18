import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Define the signals to be visualized
signal = "111100010"
signal_2 = "0100110011"
plots = []  # List of plotting functions
titles = [] # Titles for each graph

# === Plotting Functions ===

# Plot NRZ-L signal
def plot_nrz_l(signal, ax):
    X, Y = [], []   # Initialize X and Y coordinates
    # Define voltage levels based on the bits
    levels = [1 if bit == '1' else 0 for bit in signal] 
    # Create step points for visualization
    for i, level in enumerate(levels):
        X.extend([i, i + 1])
        Y.extend([level, level])
    # Configure the graph
    ax.step(X, Y, where='post')
    ax.set_ylim(-0.5, 1.5)
    ax.set_title("Signal NRZ-L")
    ax.set_xlabel("Time")
    ax.set_ylabel("Voltage Level")
    ax.grid(True)
    # Add bit labels on the plot
    for idx, bit in enumerate(signal):
        ax.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)

# Plot NRZ-I signal
def plot_nrz_i(signal, ax):
    X, Y = [], []
    levels, current_level = [], 0
    # Toggle voltage on bit "1"
    for bit in signal:
        if bit == "1":
            current_level = 1 - current_level
        levels.append(current_level)
    # Create step points for visualization
    for i, level in enumerate(levels):
        X.extend([i, i + 1])
        Y.extend([level, level])
    # Configure the graph
    ax.step(X, Y, where='post')
    ax.set_ylim(-0.5, 1.5)
    ax.set_title("Signal NRZ-I")
    ax.set_xlabel("Time")
    ax.set_ylabel("Voltage Level")
    ax.grid(True)
    # Add bit labels on the plot
    for idx, bit in enumerate(signal):
        ax.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)

# Plot Bipolar AMI signal
def plot_bipolar_ami(signal, ax):
    X, Y = [], []
    levels, last_non_zero = [], -1
    # Alternate between +1 and -1 on bit "1"
    for bit in signal:
        if bit == "1":
            last_non_zero *= -1
            levels.append(last_non_zero)
        else:
            levels.append(0)
    # Create step points for visualization
    for i, level in enumerate(levels):
        X.extend([i, i + 1])
        Y.extend([level, level])
    # Configure the graph
    ax.step(X, Y, where='post')
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Signal Bipolar AMI")
    ax.set_xlabel("Time")
    ax.set_ylabel("Voltage Level")
    ax.grid(True)
    # Add bit labels on the plot
    for idx, bit in enumerate(signal):
        ax.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)

# Plot Pseudoternary signal
def plot_pseudoternary(signal, ax):
    X, Y = [], []
    levels, last_non_zero = [], -1
    # Alternate between +1 and -1 on bit "0"
    for bit in signal:
        if bit == "0":
            last_non_zero *= -1
            levels.append(last_non_zero)
        else:
            levels.append(0)
    for i, level in enumerate(levels):
        X.extend([i, i + 1])
        Y.extend([level, level])
    # Configure the graph
    ax.step(X, Y, where='post')
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Signal Pseudoternary")
    ax.set_xlabel("Time")
    ax.set_ylabel("Voltage Level")
    ax.grid(True)
    # Add bit labels on the plot
    for idx, bit in enumerate(signal):
        ax.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)

# Plot Manchester signal
def plot_manchester(signal, ax):
    X, Y = [], []
    # Manchester encoding: 0 -> High to Low, 1 -> Low to High
    for i, bit in enumerate(signal):
        t0, t_half, t1 = i, i + 0.5, i + 1
        # Define the transition points
        if bit == "0":
            X.extend([t0, t_half, t_half, t1])
            Y.extend([1, 1, 0, 0])
        else:
            X.extend([t0, t_half, t_half, t1])
            Y.extend([0, 0, 1, 1])
    # Configure the graph
    ax.step(X, Y, where='post', linewidth=2, color='blue')
    ax.set_ylim(-0.5, 1.5)
    ax.set_title("Manchester")
    ax.set_xlabel("Time")
    ax.set_ylabel("Voltage Level")
    ax.grid(True)
    # Add bit labels on the plot
    for idx, bit in enumerate(signal):
        ax.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)

# Plot Differential Encoding (IEEE 802.5)
def plot_differential(signal, ax):
    X, Y = [], []
    current_level = 1 # Start at level 1
    # Iterate over each bit to determine transitions
    for i, bit in enumerate(signal):
        t_start, t_mid, t_end = i, i + 0.5, i + 1
        if bit == "0":
            # Toggle the level at the start and at the midpoint
            current_level = 1 - current_level
            X.extend([t_start, t_mid])
            Y.extend([current_level, current_level])
            current_level = 1 - current_level
            X.extend([t_mid, t_end])
            Y.extend([current_level, current_level])
        else:
            # Maintain the same level until the midpoint, then toggle
            X.extend([t_start, t_mid])
            Y.extend([current_level, current_level])
            current_level = 1 - current_level
            X.extend([t_mid, t_end])
            Y.extend([current_level, current_level])
    # Configure the graph
    ax.step(X, Y, where='post', linewidth=2, color='blue')
    ax.set_ylim(-0.5, 1.5)
    ax.set_title("Differential Encoding (IEEE 802.5)")
    ax.set_xlabel("Time")
    ax.set_ylabel("Voltage Level")
    ax.grid(True)
    # Add bit labels on the plot
    for idx, bit in enumerate(signal):
        ax.text(idx + 0.5, 1.2, bit, ha='center', va='center', fontsize=8)

# Create main plot 
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

# List of graphs
plots = [
    plot_nrz_l,
    plot_nrz_i,
    plot_bipolar_ami,
    plot_pseudoternary,
    plot_manchester,
    plot_differential
]

# Initial state
index = 0
plots[index](signal, ax)

#Navegation functions
def next_plot(event):
    global index
    index = (index + 1) % len(plots)
    ax.clear()
    plots[index](signal, ax)
    plt.draw()

def prev_plot(event):
    global index
    index = (index - 1) % len(plots)
    ax.clear()
    plots[index](signal, ax)
    plt.draw()

# Navegation buttons
ax_next = plt.axes([0.8, 0.05, 0.1, 0.075])
ax_prev = plt.axes([0.1, 0.05, 0.1, 0.075])
btn_next = Button(ax_next, 'Next')
btn_prev = Button(ax_prev, 'Prev')
btn_next.on_clicked(next_plot)
btn_prev.on_clicked(prev_plot)

# Show first plot
plt.show()
