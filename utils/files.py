import time

def readLine(path: str) -> bytes:
    # The binary data in little-endian format
    with open(path, "r") as file:
        hex_data = file.readline()
        # Combine the lines into a single hexadecimal string
        hex_data = "".join(hex_data).strip()
        # Convert the hexadecimal string to bytes and add it to the array
        return bytes.fromhex(hex_data)

def readFile(path: str) -> bytes:
    full_data = []
    with open(path, 'r') as file:
        for line in file:
            data = bytes.fromhex("".join(line).strip())
            yield data

