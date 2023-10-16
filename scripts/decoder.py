import struct

# The binary data in little-endian format
data = bytes.fromhex("01000000af695604fbcf0446f8ff47449bd5c945ca9426c1b8fdd73dd63a6a4080c57f3e40f7db3d2659ca41d22c38bc9fedacbe470311bd6ddc1d3fa61a0dbda2acbf3bcf9fa13e2fdfc93e1122813e49b0113f6ac1e1bbf2b159bb4f77153f9b24c93d56769042ece69342c696964275968f4201000000000000000000000000000000000000000000000000000000000000000bd7233d0000000000000000000000007bbfdcbeed7be6beb9e636be334491beb2c6dc3e887de63ecb4d1c3f46b9993e307ba0bb00c72cba20ba1bbce06f043cdf0e000006000000840300000100000006000000e01258c35d647ec1df6cb9c2245cca41957e5f48ce5ca9437207504372135243cc634f43cc634f43295f36410000803f9eacdd459b2df7429b2df74282ec6a429ade49430100018200000002f57500000000000000000000000000000000006e000000")

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
