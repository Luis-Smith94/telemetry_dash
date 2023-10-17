import socket
import struct
import threading
import sys

# Define global variable to control the loop
exit_flag = False

# Define the UDP listener function
def udp_listener():
    HOST_IP = "0.0.0.0"
    HOST_PORT = 5300
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST_IP, HOST_PORT))

    print(f"Waiting for messages on {HOST_IP}, port {HOST_PORT}...")

    while not exit_flag:
        data, addr = s.recvfrom(BUFFER_SIZE)
        yield data.hex()  # Yield the hexadecimal data

# Define the data decoder function
def decode_data(hex_data):
    # Define the field format, field names, and other definitions as you have in your script
    # ...

    # Convert the hexadecimal string to bytes
    data = bytes.fromhex(hex_data)

    # Reset the index for each line
    index = 0

    # Unpack and print each field
    for field_name, field_format in field_definitions:
        field_size = struct.calcsize(field_format)
        field_data = data[index:index + field_size]
        field_value = struct.unpack(field_format, field_data)[0]
        print(f"{field_name}: {field_value}")
        index += field_size

# Function to handle exit command
def exit_program():
    global exit_flag
    exit_flag = True

# Main execution
if __name__ == "__main__":
    # Start a separate thread for the UDP listener
    udp_listener_thread = threading.Thread(target=udp_listener)
    udp_listener_thread.daemon = True
    udp_listener_thread.start()

    # Listen for an exit command (e.g., press "q" and Enter to exit)
    print("Press 'q' and Enter to exit.")
    while not exit_flag:
        user_input = input()
        if user_input.lower() == "q":
            exit_program()

    # Gracefully exit the program
    sys.exit(0)
