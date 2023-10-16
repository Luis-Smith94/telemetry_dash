import matplotlib.pyplot as plt

# Read data from the text file
with open('../datas/z.txt', 'r') as file:
    data = [float(line.strip()) for line in file]

# Create the X-axis values (assuming 1, 2, 3, ... for each data point)
x = list(range(1, len(data) + 1))

# Create a basic line graph
plt.plot(x, data, marker='o', linestyle='-')

# Customize the graph if needed
plt.title('Sample Data Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Save the graph as an image (optional)
plt.savefig('graph.png')

# Show the graph
plt.show()
