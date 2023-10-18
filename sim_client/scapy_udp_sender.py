from scapy.all import IP, UDP, send
import binascii

# Define source and destination IP addresses
src_ip = "127.0.0.1"
dst_ip = "127.0.0.1"

# Define source and destination ports
src_port = 5200
dst_port = 5300

# Specify your custom hexadecimal payload
hex_payload = input("hex: ? ")

# Convert the hexadecimal string to bytes
custom_data = binascii.unhexlify(hex_payload)

# Create the UDP packet
udp_packet = IP(src=src_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / custom_data

# Set the length of the UDP packet (including headers)
payload_length = len(custom_data)
udp_packet[UDP].len = payload_length + 8  # 8 bytes for UDP header

# Send the packet
send(udp_packet)
