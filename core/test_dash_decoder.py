import dash_decoder as decoder

def readFile(path: str) -> bytes:
    # The binary data in little-endian format
    data = []
    with open(path, "r") as file:
        hex_data = file.readlines()
        # Combine the lines into a single hexadecimal string
        hex_data = "".join(hex_data).strip()
        # Convert the hexadecimal string to bytes and add it to the array
        data.append(bytes.fromhex(hex_data))

    return data


res = decoder.decode_packet(readFile("datas/dataset.txt"))

for idx in range(len(res)):
    print(str(decoder.dash_packet_fields[idx][0]) + " = " + str(res[idx]))