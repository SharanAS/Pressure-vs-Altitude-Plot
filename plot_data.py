import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from itertools import count

# Load CSV data
pressure_data = pd.read_excel('Raw_Test_Flight_Data_25.xlsx')

counter = count(start=0, step=1)

# Set up plot
fig, ax = plt.subplots()
x_plot = []
y_plot = []
velocity = [0]

# Function to update the Plot Data
def update(i):
    j = next(counter)

    # Stop if counter reaches the end of data
    if j >= len(pressure_data):
        return

    # To add new points to the plot points
    new_x = j
    new_y = int((1 - (pow((pressure_data.values[j][0] / 101325), (0.190263)))) / (2.25577 / 100000))
    x_plot.append(new_x)
    y_plot.append(new_y)

    # Velocity calculation
    if len(y_plot) > 1:
        v = (y_plot[-1] - y_plot[-2]) / (x_plot[-1] - x_plot[-2])
        velocity.append(v)

    # to clear the plot and redraw it
    ax.clear()
    ax.plot(x_plot, y_plot, marker='o', label="Altitude")
    ax.plot(x_plot, velocity, marker='o', label="Velocity")

    # To add x and y labels, title and grid to the plot
    ax.set_xlabel("Time")
    ax.set_ylabel("Altitude / Velocity")
    ax.set_title("Time vs Altitude and Velocity")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()

# To graph the new plot data
ani = FuncAnimation(fig, update, interval=1000)

# To show the plotted graph
plt.show()
