import pygame
import sys
import time
import numpy as np
sys.path.insert(0, ".")

import core.dash_decoder as decoder
import core.udp_receiver as rcv
import utils.files as files
import numpy as np

sys.path.insert(0, ".")

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_size = (800, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Real-Time Plot")

# Colors
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Initialize data arrays
brake_data = np.array([], dtype=float)
accel_data = np.array([], dtype=float)
x_axis = np.array([], dtype=int)

# Variable to store the timestamp of the last data processing
last_processing_time = time.time()

# Set the desired processing interval in seconds (e.g., 0.1 seconds)
processing_interval = 0.1

def update_dashboard_brake_accel():
    screen.fill(black)  # Clear the screen

    # Draw the acceleration and brake data
    for i in range(1, len(x_axis)):
        pygame.draw.line(screen, blue, (x_axis[i - 1], brake_data[i - 1]), (x_axis[i], brake_data[i]), 2)
        pygame.draw.line(screen, red, (x_axis[i - 1], accel_data[i - 1]), (x_axis[i], accel_data[i]), 2)

    pygame.display.flip()

# Your decoder and receiver setup here
HOST_IP = "127.0.0.1"
HOST_PORT = 5300

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate receiving data, replace with your actual data reception
    # decoded_data = your_decode_function(data)
    # brake = decoded_data.get("Brake", -1) / 255.0 * 100
    # accel = decoded_data.get("Accel", -1) / 255.0 * 100
    for data in rcv.listen(HOST_IP, HOST_PORT):
        decoded_data = decoder.decode_packet(data)
        brake = decoded_data.get("Brake", -1) / 255.0 * 100
        accel = decoded_data.get("Accel", -1) / 255.0 * 100

        brake_data = np.append(brake_data, brake)
        accel_data = np.append(accel_data, accel)
        x_axis = np.append(x_axis, len(accel_data))

    # Check if it's time to process the data
    current_time = time.time()
    if current_time - last_processing_time >= processing_interval:
        update_dashboard_brake_accel()
        last_processing_time = current_time

    # Add a delay to control the refresh rate
    pygame.time.delay(10)  # Adjust the delay time as needed

pygame.quit()
sys.exit()
