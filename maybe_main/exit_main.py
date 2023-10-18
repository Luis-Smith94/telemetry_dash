import socket
import struct
import threading
import sys

# Define global variable to control the loop
exit_flag = False

# Define the UDP listener function
def udp_listener():
    HOST_IP = "0.0.0.0"
    HOST_PORT = 5300
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST_IP, HOST_PORT))

    print(f"Waiting for messages on {HOST_IP}, port {HOST_PORT}...")

    while not exit_flag:
        try:
            data, addr = s.recvfrom(BUFFER_SIZE)
            yield data.hex()  # Yield the hexadecimal data
        except KeyboardInterrupt:
            break

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

# Function to handle exit command
def exit_program():
    global exit_flag
    exit_flag = True

# Main execution
if __name__ == "__main__":
    # Start a separate thread for the UDP listener
    udp_listener_thread = threading.Thread(target=udp_listener)
    udp_listener_thread.daemon = True
    udp_listener_thread.start()

    print("Press 'q' and Enter to exit.")

    while not exit_flag:
        try:
            user_input = input()
            if user_input.lower() == "q":
                exit_program()
        except KeyboardInterrupt:
            exit_program()

    # Gracefully exit the program
    sys.exit(0)
