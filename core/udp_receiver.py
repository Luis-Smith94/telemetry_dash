import socket

"""
HOST_IP = "0.0.0.0"
HOST_PORT = 5300
"""
BUFFER_SIZE = 4094

"""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST_IP, HOST_PORT))

print(f"Attente de message sur {HOST_IP}, port {HOST_PORT}...")
while True:
    data, addr = s.recvfrom(BUFFER_SIZE)
    print(data.hex())
# print(data)
"""

def listen(ip: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip, port))
    s.settimeout(30)

    print(f"Attente de message sur {ip}, port {port}...")
    while True:
        try:
            data, addr = s.recvfrom(BUFFER_SIZE)
            # print("Message reçu")
            yield data
        except:
            print("Reception timeout: stop")
            s.close()
            return 

def listenOnce(ip: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip, port))
    s.settimeout(30)

    print(f"Attente de message sur {ip}, port {port}...")
    try:
        data, addr = s.recvfrom(BUFFER_SIZE)
        # print("Message reçu")
        return data
    except:
        print("Reception timeout: stop")
        s.close()
        return None
        



