import sys
sys.path.insert(0,".")

import dash_decoder as decoder
import utils.files as files

line = files.readLine("datas/one_dataset.txt")
print(line)
res = decoder.decode_packet(line)
for k, v in res.items():
    print(f"{k}  = {v}")

print("=========================================================================")

full_file = files.readFile("datas/one_dataset.txt")
print(full_file)
for line in full_file:
    res = decoder.decode_packet(line)
    for k, v in res.items():
        print(f"{k}  = {v}")