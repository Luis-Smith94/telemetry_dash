import socket
import struct
import matplotlib.pyplot as plt

# Define the UDP listener function
def udp_listener():
    HOST_IP = "0.0.0.0"
    HOST_PORT = 5300
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST_IP, HOST_PORT))

    print(f"Waiting for messages on {HOST_IP}, port {HOST_PORT}...")

    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        yield data.hex()  # Yield the hexadecimal data

# Define the data decoder function
def decode_data(hex_data):
    # Define the field format, field names, and other definitions as you have in your script
    # ...
    index = 0

    # Define the field format
    field_format = "<i"  # Use "i" for signed integers and "f" for floating-point numbers

    # Define the field names and their corresponding format
    field_definitions = [
        ("IsRaceOn", "i"),
        ("TimestampMS", "I"),
        ("EngineMaxRpm", "f"),
        ("EngineIdleRpm", "f"),
        ("CurrentEngineRpm", "f"),
        ("AccelerationX", "f"),
        ("AccelerationY", "f"),
        ("AccelerationZ", "f"),
        ("VelocityX", "f"),
        ("VelocityY", "f"),
        ("VelocityZ", "f"),
        ("AngularVelocityX", "f"),
        ("AngularVelocityY", "f"),
        ("AngularVelocityZ", "f"),
        ("Yaw", "f"),
        ("Pitch", "f"),
        ("Roll", "f"),
        ("NormalizedSuspensionTravelFrontLeft", "f"),
        ("NormalizedSuspensionTravelFrontRight", "f"),
        ("NormalizedSuspensionTravelRearLeft", "f"),
        ("NormalizedSuspensionTravelRearRight", "f"),
        ("TireSlipRatioFrontLeft", "f"),
        ("TireSlipRatioFrontRight", "f"),
        ("TireSlipRatioRearLeft", "f"),
        ("TireSlipRatioRearRight", "f"),
        ("WheelRotationSpeedFrontLeft", "f"),
        ("WheelRotationSpeedFrontRight", "f"),
        ("WheelRotationSpeedRearLeft", "f"),
        ("WheelRotationSpeedRearRight", "f"),
        ("WheelOnRumbleStripFrontLeft", "i"),
        ("WheelOnRumbleStripFrontRight", "i"),
        ("WheelOnRumbleStripRearLeft", "i"),
        ("WheelOnRumbleStripRearRight", "i"),
        ("WheelInPuddleDepthFrontLeft", "f"),
        ("WheelInPuddleDepthFrontRight", "f"),
        ("WheelInPuddleDepthRearLeft", "f"),
        ("WheelInPuddleDepthRearRight", "f"),
        ("SurfaceRumbleFrontLeft", "f"),
        ("SurfaceRumbleFrontRight", "f"),
        ("SurfaceRumbleRearLeft", "f"),
        ("SurfaceRumbleRearRight", "f"),
        ("TireSlipAngleFrontLeft", "f"),
        ("TireSlipAngleFrontRight", "f"),
        ("TireSlipAngleRearLeft", "f"),
        ("TireSlipAngleRearRight", "f"),
        ("TireCombinedSlipFrontLeft", "f"),
        ("TireCombinedSlipFrontRight", "f"),
        ("TireCombinedSlipRearLeft", "f"),
        ("TireCombinedSlipRearRight", "f"),
        ("SuspensionTravelMetersFrontLeft", "f"),
        ("SuspensionTravelMetersFrontRight", "f"),
        ("SuspensionTravelMetersRearLeft", "f"),
        ("SuspensionTravelMetersRearRight", "f"),
        ("CarOrdinal", "i"),
        ("CarClass", "i"),
        ("CarPerformanceIndex", "i"),
        ("DrivetrainType", "i"),
        ("NumCylinders", "i"),
        ("PositionX", "f"),
        ("PositionY", "f"),
        ("PositionZ", "f"),
        ("Speed", "f"),
        ("Power", "f"),
        ("Torque", "f"),
        ("TireTempFrontLeft", "f"),
        ("TireTempFrontRight", "f"),
        ("TireTempRearLeft", "f"),
        ("TireTempRearRight", "f"),
        ("Boost", "f"),
        ("Fuel", "f"),
        ("DistanceTraveled", "f"),
        ("BestLap", "f"),
        ("LastLap", "f"),
        ("CurrentLap", "f"),
        ("CurrentRaceTime", "f"),
        ("LapNumber", "H"),
        ("RacePosition", "B"),
        ("Accel", "B"),
        ("Brake", "B"),
        ("Clutch", "B"),
        ("HandBrake", "B"),
        ("Gear", "B"),
        ("Steer", "b"),
        ("NormalizedDrivingLine", "b"),
        ("NormalizedAIBrakeDifference", "b"),
        ("TireWearFrontLeft", "f"),
        ("TireWearFrontRight", "f"),
        ("TireWearRearLeft", "f"),
        ("TireWearRearRight", "f"),
        ("TrackOrdinal", "i")
    ]

    # Convert the hexadecimal string to bytes
    data = bytes.fromhex(hex_data)

    decoded_data = {}  # Create a dictionary to store the decoded data

    # Unpack and store each field in the dictionary
    for field_name, field_format in field_definitions:
        field_size = struct.calcsize(field_format)
        field_data = data[index:index + field_size]
        field_value = struct.unpack(field_format, field_data)[0]
        decoded_data[field_name] = field_value
        index += field_size

    return decoded_data



# Initialize empty lists to store the coordinates
x_coords = []
y_coords = []
z_coords = []

# Create a function to update the plot with new data
def update_plot(decoded_data):
    try:
        # Split the decoded_data into field_name and field_value
        data_fields = decoded_data.split(': ')
        if len(data_fields) != 2:
            raise ValueError("Invalid data format")

        field_name, field_value = data_fields
        field_value = float(field_value)

        # Check the field name and update the corresponding coordinate list
        if field_name == 'PositionX':
            x_coords.append(field_value)
        elif field_name == 'PositionY':
            y_coords.append(field_value)
        elif field_name == 'PositionZ':
            z_coords.append(field_value)
        else:
            print(f"Unknown field: {field_name}")

        # Plot the updated data
        plt.figure(figsize=(8, 6))
        plt.plot(x_coords, label='PositionX')
        plt.plot(y_coords, label='PositionY')
        plt.plot(z_coords, label='PositionZ')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Position')
        plt.legend()
        plt.grid()
        plt.title('Real-time XYZ Coordinates')
        plt.show()

    except ValueError as e:
        print(f"Error: {e}")

# Example usage of the function (replace this with your real-time data source)
# decoded_data = "PositionX: 498.3065490722656"
# update_plot(decoded_data)

# You can call update_plot(decoded_data) whenever you receive new data


# Main execution
if __name__ == "__main__":
    for hex_data in udp_listener():
        decoded_data = decode_data(hex_data)
        update_plot(decoded_data)
