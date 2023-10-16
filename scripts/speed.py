import struct

# Open the file and read the lines
with open("datas/dataset.txt", "r") as file:
    lines = file.readlines()

# Define the field format for "Speed" as a float (assuming it is a float)
Speed_format = "<f"
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
# Find the index of the "Speed" field in the field_definitions list
Speed_index = next((i for i, (name, fmt) in enumerate(field_definitions) if name == "Speed"), None)

# Iterate through the lines and process each one
for line in lines:
    # Remove any leading/trailing whitespace and convert to a hexadecimal string
    hex_data = line.strip()

    # Convert the hexadecimal string to bytes
    data = bytes.fromhex(hex_data)

    # Unpack the "Speed" field based on its index in field_definitions
    field_name, field_format = field_definitions[Speed_index]

    field_size = struct.calcsize(field_format)
    field_data = data[Speed_index * field_size:(Speed_index + 1) * field_size]
    field_value = struct.unpack(field_format, field_data)[0]
    print(f"{field_name}: {field_value}")
