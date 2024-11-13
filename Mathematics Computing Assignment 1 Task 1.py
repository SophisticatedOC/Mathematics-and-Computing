import numpy as np
import matplotlib.pyplot as plt

# Initial constants
j = 1j  # imaginary
alpha = 37
u = np.sqrt(2) / (1 + j)  # complex number u

# initial position z_initial
z_initial = (1 + j) / (np.sqrt(2) * j**4 * (1 * j) / abs(1 + j) * alpha)

# 64 times
positions = [z_initial]
for _ in range(63):
    positions.append(positions[-1] / u)

# mean position
mean_position = sum(positions) / len(positions)

# integer coordinates of the key card
key_card_x = int(mean_position.real)
key_card_y = int(mean_position.imag)

# Plotting path and mean
x_vals = [pos.real for pos in positions]
y_vals = [pos.imag for pos in positions]

plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='o', color='blue', linestyle='-', markersize=4, label='Path of DI Irrational')
plt.plot(mean_position.real, mean_position.imag, 'rx', markersize=10, label='Mean Position')
plt.title("Path of DI Irrational's Movement and Mean Position")
plt.xlabel("Real Axis (X)")
plt.ylabel("Imaginary Axis (Y)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.grid()
plt.show()

# integer coords of the key card position
key_card_x, key_card_y