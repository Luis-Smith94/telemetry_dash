import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST_IP, HOST_PORT))

print(f"Attente de message sur {HOST_IP}, port {HOST_PORT}...")
data, addr = s.recvfrom(BUFFER_SIZE)