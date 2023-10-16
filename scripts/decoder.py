import struct

# The binary data in little-endian format
data = bytes.fromhex("01000000af695604fbcf0446f8ff47449bd5c945ca9426c1b8fdd73dd63a6a4080c57f3e40f7db3d2659ca41d22c38bc9fedacbe470311bd6ddc1d3fa61a0dbda2acbf3bcf9fa13e2fdfc93e1122813e49b0113f6ac1e1bbf2b159bb4f77153f9b24c93d56769042ece69342c696964275968f4201000000000000000000000000000000000000000000000000000000000000000bd7233d0000000000000000000000007bbfdcbeed7be6beb9e636be334491beb2c6dc3e887de63ecb4d1c3f46b9993e307ba0bb00c72cba20ba1bbce06f043cdf0e000006000000840300000100000006000000e01258c35d647ec1df6cb9c2245cca41957e5f48ce5ca9437207504372135243cc634f43cc634f43295f36410000803f9eacdd459b2df7429b2df74282ec6a429ade49430100018200000002f57500000000000000000000000000000000006e000000")

# Define the format for each 32-bit field (little-endian)
field_format = "<I"

# Calculate the total size of the data
total_size = struct.calcsize(field_format) * len(data) // 4

# Check if the total size matches the actual data size
if total_size != len(data):
    raise ValueError("Data size does not match the expected size")

# Unpack the data and reverse the endianness for each field
fields = struct.unpack("<" + "I" * len(data) // 4, data)

# Define the names for each field
field_names = [f"Field{i+1}" for i in range(len(fields))]

# Print each field's value
for name, value in zip(field_names, fields):
    print(f"{name}: {value}")
