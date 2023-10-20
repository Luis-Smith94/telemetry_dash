import matplotlib.pyplot as plt
import sys
import time  # Import the time module
import datetime as dt
import matplotlib.animation as animation
sys.path.insert(0, ".")

import core.dash_decoder as decoder
import core.udp_receiver as rcv
import utils.files as files
import numpy as np

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(211)
bx = fig.add_subplot(212)
xs = []
yas = []
ybs = []

def bus():
    HOST_IP = "127.0.0.1"
    HOST_PORT = 5300
    for data in rcv.listen(HOST_IP, HOST_PORT):
        decoded_data = decoder.decode_packet(data)
        brake = decoded_data.get("Brake", -1) / 255.0 * 100
        return brake


# This function is called periodically from FuncAnimation
def animate(i, xs, yas, ybs):

    HOST_IP = "127.0.0.1"
    HOST_PORT = 5300
    data = rcv.listenOnce(HOST_IP, HOST_PORT)
    decoded_data = decoder.decode_packet(data)
    # Read temperature (Celsius) from TMP102
    brake = decoded_data.get("Brake", -1) / 255*100
    accel = decoded_data.get("Accel", -1) / 255*100
    TimestampMS = decoded_data.get("CurrentRaceTime", -1)

    # Add x and y to lists
    xs.append(TimestampMS)
    yas.append(brake)
    ybs.append(accel)

    # Limit x and y lists to 20 items
    xs = xs[-200:]
    yas = yas[-200:]
    ybs = ybs[-200:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, yas, label='Accel', color='red')
    bx.clear()
    bx.plot(xs, ybs, label='Accel', color='green')

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    # plt.title('Breaking pressure over Time')
    # plt.ylabel('Breaking pressure (%)')
    plt.ylim(-5,105)

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, yas, ybs), interval=0.0001)
plt.show()
