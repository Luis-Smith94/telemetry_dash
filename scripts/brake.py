import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Initialize an empty list to store brake intensity values
intensity_values = []

# Read data from the text file
with open('brake_data.txt', 'r') as file:
    for line in file:
        intensity = float(line.strip())
        intensity_values.append(intensity)

# Create a time sequence as the x-axis
time_values = list(range(len(intensity_values)))

# Define the color map for intensity values
cmap = LinearSegmentedColormap.from_list('intensity', ['blue', 'red'])

# Normalize the intensity values to use the colormap
norm = plt.Normalize(min(intensity_values), max(intensity_values))

# Create a line graph
plt.plot(time_values, intensity_values, color='gray', linestyle='-')

# Create a scatter plot with color mapping
plt.scatter(time_values, intensity_values, c=intensity_values, cmap=cmap, norm=norm)
plt.colorbar(label='Brake Intensity')

# Customize the graph
plt.title('Brake Intensity Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Intensity')

# Set axis limits
plt.xlim(0, len(intensity_values))  # Adjust these limits as needed for the x-axis
plt.ylim(0, 100)  # Adjust these limits as needed for the y-axis

# Show the graph
plt.show()
