import struct

dash_packet_fields = [
    ("IsRaceOn", "S32"),
    ("TimestampMS", "U32"),
    ("EngineMaxRpm", "F32"),
    ("EngineIdleRpm", "F32"),
    ("CurrentEngineRpm", "F32"),
    ("AccelerationX", "F32"),
    ("AccelerationY", "F32"),
    ("AccelerationZ", "F32"),
    ("VelocityX", "F32"),
    ("VelocityY", "F32"),
    ("VelocityZ", "F32"),
    ("AngularVelocityX", "F32"),
    ("AngularVelocityY", "F32"),
    ("AngularVelocityZ", "F32"),
    ("Yaw", "F32"),
    ("Pitch", "F32"),
    ("Roll", "F32"),
    ("NormalizedSuspensionTravelFrontLeft", "F32"),
    ("NormalizedSuspensionTravelFrontRight", "F32"),
    ("NormalizedSuspensionTravelRearLeft", "F32"),
    ("NormalizedSuspensionTravelRearRight", "F32"),
    ("TireSlipRatioFrontLeft", "F32"),
    ("TireSlipRatioFrontRight", "F32"),
    ("TireSlipRatioRearLeft", "F32"),
    ("TireSlipRatioRearRight", "F32"),
    ("WheelRotationSpeedFrontLeft", "F32"),
    ("WheelRotationSpeedFrontRight", "F32"),
    ("WheelRotationSpeedRearLeft", "F32"),
    ("WheelRotationSpeedRearRight", "F32"),
    ("WheelOnRumbleStripFrontLeft", "S32"),
    ("WheelOnRumbleStripFrontRight", "S32"),
    ("WheelOnRumbleStripRearLeft", "S32"),
    ("WheelOnRumbleStripRearRight", "S32"),
    ("WheelInPuddleDepthFrontLeft", "F32"),
    ("WheelInPuddleDepthFrontRight", "F32"),
    ("WheelInPuddleDepthRearLeft", "F32"),
    ("WheelInPuddleDepthRearRight", "F32"),
    ("SurfaceRumbleFrontLeft", "F32"),
    ("SurfaceRumbleFrontRight", "F32"),
    ("SurfaceRumbleRearLeft", "F32"),
    ("SurfaceRumbleRearRight", "F32"),
    ("TireSlipAngleFrontLeft", "F32"),
    ("TireSlipAngleFrontRight", "F32"),
    ("TireSlipAngleRearLeft", "F32"),
    ("TireSlipAngleRearRight", "F32"),
    ("TireCombinedSlipFrontLeft", "F32"),
    ("TireCombinedSlipFrontRight", "F32"),
    ("TireCombinedSlipRearLeft", "F32"),
    ("TireCombinedSlipRearRight", "F32"),
    ("SuspensionTravelMetersFrontLeft", "F32"),
    ("SuspensionTravelMetersFrontRight", "F32"),
    ("SuspensionTravelMetersRearLeft", "F32"),
    ("SuspensionTravelMetersRearRight", "F32"),
    ("CarOrdinal", "S32"),
    ("CarClass", "S32"),
    ("CarPerformanceIndex", "S32"),
    ("DrivetrainType", "S32"),
    ("NumCylinders", "S32"),
    ("PositionX", "F32"),
    ("PositionY", "F32"),
    ("PositionZ", "F32"),
    ("Speed", "F32"),
    ("Power", "F32"),
    ("Torque", "F32"),
    ("TireTempFrontLeft", "F32"),
    ("TireTempFrontRight", "F32"),
    ("TireTempRearLeft", "F32"),
    ("TireTempRearRight", "F32"),
    ("Boost", "F32"),
    ("Fuel", "F32"),
    ("DistanceTraveled", "F32"),
    ("BestLap", "F32"),
    ("LastLap", "F32"),
    ("CurrentLap", "F32"),
    ("CurrentRaceTime", "F32"),
    ("LapNumber", "U16"),
    ("RacePosition", "U8"),
    ("Accel", "U8"),
    ("Brake", "U8"),
    ("Clutch", "U8"),
    ("HandBrake", "U8"),
    ("Gear", "U8"),
    ("Steer", "S8"),
    ("NormalizedDrivingLine", "S8"),
    ("NormalizedAIBrakeDifference", "S8"),
    ("TireWearFrontLeft", "F32"),
    ("TireWearFrontRight", "F32"),
    ("TireWearRearLeft", "F32"),
    ("TireWearRearRight", "F32"),
    ("TrackOrdinal", "S32")
]                                                                                                                         

format_and_size = [["S32", "F32", "U32", "U16", "U8", "S8"],
                   [4, 4, 4, 2, 1, 1]]

DASH_PAYLOAD_SIZE = 331

def getFormatSize(format: str):
    return format_and_size[1][format_and_size[0].index(format)]

def decode(data: bytes, idx: int, format: str):
    size = getFormatSize(format)
    
    if format == "F32":
        return struct.unpack('<f', data[idx:idx+size])
    
    return int.from_bytes(data[idx:idx+size], byteorder="little", signed=(format[0] == 'S'))

def decode_packet(data: bytes):
    idx = 0
    res = []
    for field in dash_packet_fields:
        res.append(decode(data, idx, field[1]))
        idx += getFormatSize(field[1])

    print(f"Final idx = {idx}")
    return res

