import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
sys.path.insert(0,".")


import core.dash_decoder as decoder
import core.udp_receiver as rcv
import utils.files as files

brake_data = []
accel_data = []
x_axis = []
 
# Create a function to update the dashboard
def update_dashboard_brake_accel():
    # Clear the existing plot
    plt.clf()


    # Plot acceleration, brake, and fuel data over time
    plt.plot(x_axis, brake_data, label='Brake', color='blue')
    plt.plot(x_axis, accel_data, label='Accel', color='red')

    # Add labels and legends
    #plt.xlabel('x')
    #plt.ylabel('y')
    #plt.legend()
    plt.pause(0.000000000001)

"""for data in files.readFile("datas/dataset.txt"):
    brake = decoder.decode_packet(data).get("Brake", -1)/255.0 *100
    brake_data.append(brake)
    accel = decoder.decode_packet(data).get("Accel", -1)/255.0 *100
    accel_data.append(accel)

update_dashboard_brake_accel()"""


HOST_IP = "127.0.0.1"
HOST_PORT = 5300
for data in rcv.listen(HOST_IP, HOST_PORT):
    brake = decoder.decode_packet(data).get("Brake", -1)/255.0 *100
    brake_data.append(brake)
    accel = decoder.decode_packet(data).get("Accel", -1)/255.0 *100
    accel_data.append(accel)
    x_axis.append(len(accel_data))
    update_dashboard_brake_accel()
