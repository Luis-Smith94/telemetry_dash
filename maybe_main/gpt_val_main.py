import matplotlib.pyplot as plt
import sys
import time  # Import the time module

sys.path.insert(0, ".")

import core.dash_decoder as decoder
import core.udp_receiver as rcv
import utils.files as files
import numpy as np


brake_data = np.array([])
accel_data = np.array([])
laptimes = np.array([])

# Variable to store the timestamp of the last data processing
last_processing_time = time.time()

def update_dashboard_brake_accel():
    plt.clf()
    plt.plot(laptimes, brake_data, label='Brake', color='blue')
    plt.plot(laptimes, accel_data, label='Accel', color='red')
    plt.legend()
    plt.pause(0.00000001)

HOST_IP = "127.0.0.1"
HOST_PORT = 5300

for data in rcv.listen(HOST_IP, HOST_PORT):
    decoded_data = decoder.decode_packet(data)

    brake_data = np.append(brake_data, decoded_data.get("Brake", -1) / 255.0 * 100)
    accel_data = np.append(accel_data, decoded_data.get("Accel", -1) / 255.0 * 100)
    laptimes = np.append(laptimes, decoded_data.get("CurrentRaceTime", -1))

    brake_data = brake_data[-100:]
    accel_data = accel_data[-100:]
    laptimes = laptimes[-100:]

    # Check if it's time to process the data
    update_dashboard_brake_accel()