import socket

HOST_IP = "0.0.0.0"
HOST_PORT = 5300
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST_IP, HOST_PORT))

print(f"Attente de message sur {HOST_IP}, port {HOST_PORT}...")
while True:
    data, addr = s.recvfrom(BUFFER_SIZE)
    print(data.hex())
# print(data)

