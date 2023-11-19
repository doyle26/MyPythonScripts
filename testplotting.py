import matplotlib.pyplot as plt
import sys

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y, label='Line Plot')

# Add labels and a legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Matplotlib Line Plot')
ax.legend()

# Add grid lines
ax.grid(True)

# Show the plot
plt.show()

# End
sys.exit()
