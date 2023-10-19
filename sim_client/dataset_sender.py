import socket
import time
import sys
sys.path.insert(0,".")

import utils.files as files

def send_dataset_to(path: str, ip: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in files.readFile(path):
        s.sendto(data, (ip, port))
        time.sleep(1.0/60)

    s.close()

send_dataset_to("datas/dataset.txt", "127.0.0.1", 5300)