Sharan_2025AAPS0285H_Avionics

# Pressure-vs-Altitude-Plot
A Plot of Flight Altitude(Calculated) vs Time and Velocity of flight(calculated ) vs time.


The altitude was calculated from the given Pressure data using the formula-

H = (1-((Pressure/10132.5)^(1/5.25588)))/(2.25577/100000)
The formula was taken from the website - https://www.engineeringtoolbox.com/air-altitude-pressure-d_462.html

velocity was calculated using the formula ---- ((current altitude)-(previous altitude))/1

The Excel file is then read by the python script -- plot_data.py -- line by line and plotted using the library MatPlotLib, updated every 1 second.

**Note that I have tried to smoothen the graph by extrapolating when values were missing or taking averages whenever the values were too inconsistent with flight path. But I have kept the graph non-parabloic where it needs to be ----- when the rocket is still accelerating and right after the apoogee where the parachute opens and the rocket reaches terminal velocity**

**Also note that here the initial values are removed and not plotted repeatedly to keep Franklin invested.**
