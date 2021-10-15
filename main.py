"""
Matthew Nanas
Professor Hou
Statics
October 14, 2021

This file is written for STATICS PROJECT 1 and displays 4 graphs for the magnitude of the moment and its
respective components. Additionally, data is written to an excel file for better datapoint viewing
all code has been entirely written by me.

To get started:
pip install matplotlib
pip install mplot3d
pip install numpy
pip install pandas
python main.py
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Arrays
angle = []
moment_X = []
moment_Y = []
moment_Z = []
moment_Magnitude = []

radius_Z = 2.4

# Append radii
for i in range(0, 185, 5):
    # Calculations
    theta = np.radians(i)
    angle.append(i)
    Mox = (-480 * (np.sqrt(1.2*np.cos(theta)*1.2*np.cos(theta)) + (1-1.2*np.sin(theta)*1-1.2*np.sin(theta)) - 2.408)*(1-1.2*np.sin(theta))/(np.sqrt(1.2*np.cos(theta)*1.2*np.cos(theta)) + (1-1.2*np.sin(theta)*1-1.2*np.sin(theta))))
    Moy = (576 * (np.sqrt(1.2*np.cos(theta)*1.2*np.cos(theta)) + (1-1.2*np.sin(theta)*1-1.2*np.sin(theta)) - 2.408)*(np.cos(theta))/(np.sqrt(1.2*np.cos(theta)*1.2*np.cos(theta)) + (1-1.2*np.sin(theta)*1-1.2*np.sin(theta))))
    Moz = (240 * (np.sqrt(1.2*np.cos(theta)*1.2*np.cos(theta)) + (1-1.2*np.sin(theta)*1-1.2*np.sin(theta)) - 2.408)*(np.cos(theta))/(np.sqrt(1.2*np.cos(theta)*1.2*np.cos(theta)) + (1-1.2*np.sin(theta)*1-1.2*np.sin(theta))))
    Mo = np.sqrt((Mox**2 + Moy**2 + Moz**2))

    # Add to arrays
    moment_X.append(Mox)
    moment_Y.append(Moy)
    moment_Z.append(Moz)
    moment_Magnitude.append(Mo)

# Write data to excel
excel = [angle, moment_Magnitude, moment_X, moment_Y, moment_Z]
write = pd.DataFrame(excel).T
write.to_excel(excel_writer = "./data.xlsx")

# Display data
graphs, fig = plt.subplots(4)
graphs.suptitle("Moment Components")
fig[0].plot(angle, moment_X)
fig[0].set_title("Mxo(θ) vs. θ")
fig[0].set_xlabel("θ")
fig[0].set_ylabel("Mxo(θ)")

fig[1].plot(angle, moment_Y)
fig[1].set_title("Myo(θ) vs. θ")
fig[1].set_xlabel("θ")
fig[1].set_ylabel("Myo(θ)")

fig[2].plot(angle, moment_Z)
fig[2].set_title("Mzo(θ) vs. θ")
fig[2].set_xlabel("θ")
fig[2].set_ylabel("Mzo(θ)")

fig[3].plot(angle, moment_Magnitude)
fig[3].set_title("Mo(θ) vs. θ")
fig[3].set_xlabel("θ")
fig[3].set_ylabel("Mo(θ)")

graphs.tight_layout()
plt.show()