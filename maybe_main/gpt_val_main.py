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
x_axis = np.array([])

# Variable to store the timestamp of the last data processing
last_processing_time = time.time()

def update_dashboard_brake_accel():
    plt.clf()
    plt.plot(x_axis, brake_data, label='Brake', color='blue')
    plt.plot(x_axis, accel_data, label='Accel', color='red')
    plt.legend()
    plt.pause(0.00000001)

HOST_IP = "127.0.0.1"
HOST_PORT = 5300

for data in rcv.listen(HOST_IP, HOST_PORT):
    decoded_data = decoder.decode_packet(data)
    brake = decoded_data.get("Brake", -1) / 255.0 * 100
    accel = decoded_data.get("Accel", -1) / 255.0 * 100

    brake_data = np.append(brake_data, brake)
    accel_data = np.append(accel_data, accel)
    x_axis = np.append(x_axis, len(accel_data))

    # Check if it's time to process the data
    update_dashboard_brake_accel()