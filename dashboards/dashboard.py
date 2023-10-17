import matplotlib.pyplot as plt
import numpy as np

# Initialize data arrays for real-time data storage
timestamps = []  # Timestamps for the x-axis
acceleration_data = []
brake_data = []
fuel_data = []

# Create a function to update the dashboard
def update_dashboard():
    # Clear the existing plot
    plt.clf()

    # Plot acceleration, brake, and fuel data over time
    plt.plot(timestamps, acceleration_data, label='Acceleration', color='blue')
    plt.plot(timestamps, brake_data, label='Brake', color='red')
    plt.plot(timestamps, fuel_data, label='Fuel', color='green')

    # Add labels and legends
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()

    # Display the plot
    plt.pause(0.01)  # This allows for real-time updates

# Create a loop to continuously update the dashboard with real-time data
while True:
    # Replace the following lines with your actual data ingestion mechanism
    # Here, we are simulating data for acceleration, brake, and fuel
    timestamp = np.random.randint(0, 100)  # Simulated timestamp
    acceleration = np.random.uniform(0, 1)  # Simulated acceleration data
    brake = np.random.uniform(0, 1)  # Simulated brake data
    fuel = np.random.uniform(0, 1)  # Simulated fuel data

    # Append the data to the arrays
    timestamps.append(timestamp)
    acceleration_data.append(acceleration)
    brake_data.append(brake)
    fuel_data.append(fuel)

    # Limit the number of data points displayed for better performance
    if len(timestamps) > 100:
        timestamps.pop(0)
        acceleration_data.pop(0)
        brake_data.pop(0)
        fuel_data.pop(0)

    # Call the function to update the dashboard
    update_dashboard()

# Keep the dashboard open
plt.show()
