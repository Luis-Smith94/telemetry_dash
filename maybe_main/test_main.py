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
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def bus():
    HOST_IP = "127.0.0.1"
    HOST_PORT = 5300
    for data in rcv.listen(HOST_IP, HOST_PORT):
        decoded_data = decoder.decode_packet(data)
        brake = decoded_data.get("Brake", -1) / 255.0 * 100
        return brake


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    HOST_IP = "127.0.0.1"
    HOST_PORT = 5300
    data = rcv.listenOnce(HOST_IP, HOST_PORT)
    decoded_data = decoder.decode_packet(data)
    # Read temperature (Celsius) from TMP102
    brake = decoded_data.get("Brake", -1) / 255*100
    TimestampMS = decoded_data.get("TimestampMS", -1)

    # Add x and y to lists
    xs.append(TimestampMS)
    ys.append(brake)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')
    plt.ylim(0,100)

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=0.0001)
plt.show()
