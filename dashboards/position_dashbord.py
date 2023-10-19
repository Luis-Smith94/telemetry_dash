import sys
sys.path.insert(0,".")

import matplotlib.pyplot as plt

import core.dash_decoder as decoder
import utils.files as files

position_x = []
position_y = []

# Create a function to update the dashboard
def update_dashboard_position():
    # Clear the existing plot
    plt.clf()

    # Plot acceleration, brake, and fuel data over time
    plt.plot(position_x, position_y, label='Position', color='grey')

    # Add labels and legends
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # Display the plot
    #plt.pause(0.000000000001)  # This allows for real-time updates
    plt.show(block=True)

    
def print_pos_dash():
    for data in files.readFile("datas/dataset.txt"):
        pos_x = decoder.decode_packet(data).get("PositionX", 0)
        pos_y = decoder.decode_packet(data).get("PositionY", 0)
        #print("x, y : (" + str(pos_x) + ", " + str(pos_y) + ")")
        position_x.append(pos_x)
        position_y.append(pos_y)

    update_dashboard_position()