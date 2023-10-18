import dash_decoder as decoder

def readLine(path: str) -> bytes:
    # The binary data in little-endian format
    #data = []
    #print("==================================================")
    with open(path, "r") as file:
        hex_data = file.readline()
        # Combine the lines into a single hexadecimal string
        hex_data = "".join(hex_data).strip()
        # Convert the hexadecimal string to bytes and add it to the array
        return bytes.fromhex(hex_data)
        #print(data)
        #print("-----------------------------------------------------------")
    #print("-----------------------------------------------------------")
    #return data

def readFile(path: str) -> bytes:
    full_data = []
    with open(path, 'r') as file:
        for line in file:
            full_data.append(bytes.fromhex("".join(line).strip()))

    return full_data

line = readLine("datas/one_dataset.txt")
print(line)
res = decoder.decode_packet(line)

for idx in range(len(res)):
    print(str(decoder.dash_packet_fields[idx][0]) + " = " + str(res[idx]))

print("=========================================================================")

full_file = readFile("datas/one_dataset.txt")
print(full_file)
for line in full_file:
    res = decoder.decode_packet(line)
    for idx in range(len(res)):
        print(str(decoder.dash_packet_fields[idx][0]) + " = " + str(res[idx]))