import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

from util import readfile,kml_generation

data = readfile("bronx.csv")

# =============================================Overall stats======================================
print("Total accidents:", data.shape[0])
print("Accidents in June 2017: ", data[np.logical_and(data.MONTH == 6, data.YEAR == 2017)].shape[0])
print("Accidents in July 2017: ", data[np.logical_and(data.MONTH == 7, data.YEAR == 2017)].shape[0])
print("Accidents in June 2018: ", data[np.logical_and(data.MONTH == 6, data.YEAR == 2018)].shape[0])
print("Accidents in July 2018: ", data[np.logical_and(data.MONTH == 7, data.YEAR == 2018)].shape[0])


# ===================================Location of accidents========================================
lat = data["LATITUDE"]
lon = data["LONGITUDE"]
kml_generation(lat, lon)



# =============Getting number of accidents by the hour stats=======================================
hours = range(24)
num_accidents = []
for hour in hours:
	num_accidents.append(data[data.HOUR == hour].shape[0])

plt.plot(hours, num_accidents)
ax = plt.gca()
ax.set_xticks([hour for hour in hours], minor=True)
ax.set_yticks(num_accidents, minor = True)

for point in zip(hours, num_accidents):
	ax.annotate( "({0},{1})".format(point[0], point[1]), xy = point, textcoords = "data")

plt.xlabel("Hour of the day")
plt.ylabel("Number of accident in the hour")
plt.grid()
plt.show()

