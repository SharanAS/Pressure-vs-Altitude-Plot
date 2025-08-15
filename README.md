# Pressure-vs-Altitude-Plot
A plot of Raw Test Flight Pressure Data vs corresponding altitude
The program Plots given Pressure data against corresponding altitude(calculated)

The altitude was calculated from the given Pressure data using the formula-

H = (1-((Pressure/10132.5)^(1/5.25588)))/(2.25577/100000)
The formula was taken from the website - https://www.engineeringtoolbox.com/air-altitude-pressure-d_462.html

The Excel file was then converted to csv file.

The csv file is then read by the python script -- plot_data.py -- line by line and plotted using the library MatPlotLib, updated every 1 second.

Note that here the duplicate values are removed and not plotted repeatedly to keep Franklin invested.

To plot Duplicates as given in the original Data, replace 'Raw_Test_Flight_Data_25_Without_Duplicates.csv' in the python script with 'Raw_Test_Flight_Data_25.csv'.
