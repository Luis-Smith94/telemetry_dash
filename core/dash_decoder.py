
def decode_packet(data: bytes):
    isRaceOn =  bytes[0:4]                               # S32 ; = 1 when race is on, 0 otherwise (in menus, race stopped...)
    timestampMs = bytes[4:8]                           # U32 ; Can overflow to 0 eventually
    engineMaxRpm = bytes[8:12]                          # F32 ; Can overflow to 0 eventually
    engineIdleRpm = bytes[12:16]                        # F32 ; Can overflow to 0 eventually
    currentEngineRpm = bytes[16:20]                     # F32 ; Can overflow to 0 eventually
    accelerationX = bytes[20:24]                        # F32 ; In the car's local space ; right acceleration
    accelerationY = bytes[24:28]                        # F32 ; In the car's local space ; up accelerationv
    accelerationZ = bytes[28:32]                        # F32 ; In the car's local space ; forward acceleration
    velocityX = bytes[32:36]                            # F32 ; In the car's local space ; right velocity
    velocityY = bytes[36:40]                            # F32 ; In the car's local space ; up velocity
    velocityZ = bytes[40:44]                            # F32 ; In the car's local space ; forward velocity
    angularVelocityX = bytes[44:48]                     # F32 ; In the car's local space ; pitch
    angularVelocityY = bytes[48:52]                     # F32 ; In the car's local space ; yaw
    angularVelocityZ = bytes[52:56]                     # F32 ; In the car's local space ; roll
    yaw = bytes[56:60]                                  # F32
    pitch = bytes[60:64]                                # F32
    roll = bytes[64:68]                                 # F32
    normalizedSuspensionTravelFrontLeft = bytes[68:72]  # F32 ; Suspension travel normalized: 0.0f = max stretch; 1.0 = max compression
    normalizedSuspensionTravelFrontRight = bytes[72:76] # F32 ; Suspension travel normalized: 0.0f = max stretch; 1.0 = max compression
    normalizedSuspensionTravelRearLeft = bytes[76:80]   # F32 ; Suspension travel normalized: 0.0f = max stretch; 1.0 = max compression
    normalizedSuspensionTravelRearRight = bytes[80:84]  # F32 ; Suspension travel normalized: 0.0f = max stretch; 1.0 = max compression
    tireSlipRatioFrontLeft = bytes[84:88]               # F32 ; Tire normalized slip ratio, = 0 means 100% grip and |ratio| > 1.0 means loss of grip.
    tireSlipRatioFrontRigth = bytes[88:92]              # F32 ; Tire normalized slip ratio, = 0 means 100% grip and |ratio| > 1.0 means loss of grip.
    tireSlipRatioRearLeft = bytes[92:96]                # F32 ; Tire normalized slip ratio, = 0 means 100% grip and |ratio| > 1.0 means loss of grip.
    tireSlipRatioRearRight = bytes[96:100]              # F32 ; Tire normalized slip ratio, = 0 means 100% grip and |ratio| > 1.0 means loss of grip.
    wheelRotationSpeedFrontLeft = bytes[100:104]        # F32 ; rotation speed radians/sec
    wheelRotationSpeedFrontRigth = bytes[104:108]       # F32 ; rotation speed radians/sec
    wheelRotationSpeedRearLeft = bytes[108:112]         # F32 ; rotation speed radians/sec
    wheelRotationSpeedRearRight = bytes[112:116]        # F32 ; rotation speed radians/sec
    wheelOnRumbleStripFrontLeft = bytes[116:124]        # S32 ; = 1 when wheel is on rumble strip, = 0 when off.
    wheelOnRumbleStripFrontRight = bytes[120:124]       # S32 ; = 1 when wheel is on rumble strip, = 0 when off.
    wheelOnRumbleStripRearLeft = bytes[124:128]         # S32 ; = 1 when wheel is on rumble strip, = 0 when off.
    wheelOnRumbleStripRearRight = bytes[128:132]        # S32 ; = 1 when wheel is on rumble strip, = 0 when off.
    wheelInPuddleDepthFrontLeft = bytes[132:136]        # F32 ; = from 0 to 1, where 1 is the deepest puddle
    wheelInPuddleDepthFrontRight = bytes[136:140]       # F32 ; = from 0 to 1, where 1 is the deepest puddle
    wheelInPuddleDepthRearLeft = bytes[140:144]         # F32 ; = from 0 to 1, where 1 is the deepest puddle
    wheelInPuddleDepthRearRight = bytes[144:148]        # F32 ; = from 0 to 1, where 1 is the deepest puddle
    surfaceRumbleFrontLeft = bytes[148:152]             # F32 ; Non-dimensional surface rumble values passed to controller force feedback
    surfaceRumbleFrontRight = bytes[152:156]            # F32 ; Non-dimensional surface rumble values passed to controller force feedback
    surfaceRumbleRearLeft = bytes[156:160]              # F32 ; Non-dimensional surface rumble values passed to controller force feedback
    surfaceRumbleRearRight = bytes[160:164]             # F32 ; Non-dimensional surface rumble values passed to controller force feedback
    tireSlipAngleFrontLeft = bytes[164:168]             # F32 ; Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    tireSlipAngleFrontRight = bytes[168:172]            # F32 ; Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    tireSlipAngleRearLeft = bytes[172:176]              # F32 ; Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    tireSlipAngleRearRight = bytes[176:180]             # F32 ; Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    tireCombinedSlipAngleFrontLeft = bytes[180:184]     # F32 ; Tire Combined slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    tireCombinedSlipAngleFrontRight = bytes[184:188]    # F32 ; Tire Combined slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    tireCombinedSlipAngleRearLeft = bytes[188:192]      # F32 ; Tire Combined slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    tireCombinedSlipAngleRearRight = bytes[192:196]     # F32 ; Tire Combined slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.
    suspensionTravelMetersFrontLeft = bytes[196:200]    # F32 ; Actual suspension travel in meters
    suspensionTravelMetersFrontRight = bytes[200:204]   # F32 ; Actual suspension travel in meters
    suspensionTravelMetersRearLeft = bytes[204:208]     # F32 ; Actual suspension travel in meters
    suspensionTravelMetersRearRight = bytes[208:212]    # F32 ; Actual suspension travel in meters  
    carOrdinal = bytes[212:216]                         # S32 ; Unique ID of the car make/model
    carClass = bytes[216:220]                           # S32 ; Between 0 (D -- worst cars) and 7 (X class -- best cars) inclusive
    carPerformanceIndex = bytes[220:224]                # S32 ; Between 100 (worst car) and 999 (best car) inclusive
    drivetrainType = bytes[224:228]                     # S32 ; 0 = FWD, 1 = RWD, 2 = AWD
    numCylinders = bytes[228:232]                       # S32 ; Number of cylinders in the engine
    PositionX = bytes[232:236]                          # F32
    PositionY = bytes[236:240]                          # F32
    PositionZ = bytes[240:244]                          # F32
    Speed = bytes[244:248]                              # F32
    Power = bytes[248:252]                              # F32
    Torque = bytes[252:256]                             # F32
    TireTempFrontLeft = bytes[256:260]                  # F32
    TireTempFrontRight = bytes[260:264]                 # F32
    TireTempRearLeft = bytes[264:268]                   # F32
    TireTempRearRight = bytes[268:272]                  # F32
    Boost = bytes[272:276]                              # F32
    Fuel = bytes[276:280]                               # F32
    DistanceTraveled = bytes[280:284]                   # F32
    BestLap = bytes[284:288]                            # F32
    LastLap = bytes[288:292]                            # F32
    CurrentLap = bytes[292:296]                         # F32
    CurrentRaceTime = bytes[296:300]                    # F32
    LapNumber = bytes[300:302]                          # U16
    RacePosition = bytes[302:303]                       # U8
    Accel = bytes[303:304]                              # U8
    Brake = bytes[304:305]                              # U8
    Clutch = bytes[305:306]                             # U8
    HandBrake = bytes[306:307]                          # U8
    Gear = bytes[307:308]                               # U8
    Steer = bytes[308:309]                              # S8
    NormalizedDrivingLine = bytes[309:310]              # S8
    NormalizedAIBrakeDifference = bytes[310:311]        # S8
    TireWearFrontLeft = bytes[311:315]                  # F32
    TireWearFrontRight = bytes[315:319]                 # F32
    TireWearRearLeft = bytes[319:323]                   # F32
    TireWearRearRight = bytes[323:327]                  # F32
    TrackOrdinal = bytes[327:331]                       # S32 ; ID for track



