import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from itertools import count

# Load CSV data
data = pd.read_csv('Raw_Test_Flight_Data_25_Without_Duplicates.csv')
x_data = data['Pressure']
y_data = data['Altitude']

counter = count(start=0, step=1)

# Set up plot
fig, ax = plt.subplots()
x_plot = []
y_plot = []

#Function to update the Plot Data
def update(i):
    j = next(counter)

    # Stop if counter reaches the end of data
    if j >= len(x_data):
        return
    #To add new points to the plot points
    new_x = x_data[j]
    new_y = y_data[j]
    x_plot.append(new_x)
    y_plot.append(new_y)

	#to clear the plot and redraw it
    ax.clear()  
    ax.plot(x_plot, y_plot, marker='o')
    
    #To add x and y labels, title and grid to the plot
    ax.set_xlabel("Pressure")
    ax.set_ylabel("Altitude")
    ax.set_title("Pressure vs Altitude (Live)")
    ax.grid(True)
    plt.tight_layout()

#To graph the new plot data
ani = FuncAnimation(fig, update, interval=1000)

#To show the plotted graph
plt.show()
