import struct

# The binary data in little-endian format
with open("datas/dataset.txt", "r") as file:
    hex_data = file.readlines()

# Combine the lines into a single hexadecimal string
hex_data = "".join(hex_data).strip()

# Convert the hexadecimal string to bytes
data = bytes.fromhex(hex_data)
# Define the format for each field (little-endian)
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

# Initialize an index to keep track of where we are in the data
index = 0

# Unpack and print each field
for field_name, field_format in field_definitions:
    field_size = struct.calcsize(field_format)
    field_data = data[index:index + field_size]
    field_value = struct.unpack(field_format, field_data)[0]
    print(f"{field_name}: {field_value}")
    index += field_size
