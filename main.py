from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math

radius_X = []
radius_Y = []
radius_Z = 2.4

# Append radii
for i in range(0, 185, 5):
    radius_X.append(1.2*np.cos(np.radians(i)))
    radius_Y.append(1.2*np.sin(np.radians(i)))