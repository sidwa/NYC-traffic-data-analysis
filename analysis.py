import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

from util import readfile,kml_generation

data = readfile("bronx.csv")

# =============================================Overall stats======================================
def get_overall_stats():
	print("Total accidents:", data.shape[0])
	print("Accidents in June 2017: ", data[np.logical_and(data.MONTH == 6, data.YEAR == 2017)].shape[0])
	print("Accidents in July 2017: ", data[np.logical_and(data.MONTH == 7, data.YEAR == 2017)].shape[0])
	print("Accidents in June 2018: ", data[np.logical_and(data.MONTH == 6, data.YEAR == 2018)].shape[0])
	print("Accidents in July 2018: ", data[np.logical_and(data.MONTH == 7, data.YEAR == 2018)].shape[0])


# ===================================Location of accidents========================================
def get_heat_map():
	lat = data["LATITUDE"]
	lon = data["LONGITUDE"]
	kml_generation(lat, lon)



# =============Getting number of accidents by the hour stats=======================================
def get_acc_hour():
	hours = range(24)
	num_accidents = []
	# get the number of accident for each hour of the day.
	# 23:59 is hour 23 and so is 23:00
	for hour in hours:
		num_accidents.append(data[data.HOUR == hour].shape[0])

	plt.plot(hours, num_accidents)
	ax = plt.gca()
	ax.set_xticks([hour for hour in hours], minor=True)
	ax.set_yticks(num_accidents, minor = True)

	# annotate point on the plot
	for point in zip(hours, num_accidents):
		ax.annotate( "({0},{1})".format(point[0], point[1]), xy = point, textcoords = "data")

	plt.xlabel("Hour of the day")
	plt.ylabel("Number of accident in the hour")
	plt.grid()
	plt.show()

# =======================================vehicles involved============================================
def vehicles_involved():
	"""
		number of vehicles involved in an accident, get avg and max vehicles involved.
	"""
	num_vehicles = {}
	total_accidents = data.shape[0]

	# creates a binary data frame where value of true is set where nulls were present.
	# not viable since np.logical_and takes only 2 args
	# bin_frame = data.isnull()

	# accidents with 5 vehicels will def have foll col non null
	num_vehicles[5] = total_accidents - data["CONTRIBUTING FACTOR VEHICLE 5"].isnull().sum()

	# accidents with 4 vehicle will have have following col and also accidents involving 5 cars.  
	num_vehicles[4] = total_accidents - data["CONTRIBUTING FACTOR VEHICLE 4"].isnull().sum() - num_vehicles[5]
	num_vehicles[3] = total_accidents - data["CONTRIBUTING FACTOR VEHICLE 3"].isnull().sum() - num_vehicles[4] - num_vehicles[5]
	num_vehicles[2] = total_accidents - data["CONTRIBUTING FACTOR VEHICLE 2"].isnull().sum() - num_vehicles[3] - num_vehicles[4] - num_vehicles[5] 
	num_vehicles[1] = total_accidents - num_vehicles[2] - num_vehicles[3] - num_vehicles[4] - num_vehicles[5] 
	accidents = []
	accidents.append(num_vehicles[1])
	accidents.append(num_vehicles[2])
	accidents.append(num_vehicles[3])
	accidents.append(num_vehicles[4])
	accidents.append(num_vehicles[5])


	plt.plot(range(1,6), accidents)
	ax = plt.gca()
	ax.set_xticks(range(1,6), minor=True)
	ax.set_yticks(accidents, minor=True)

	# annotate point on the plot
	for point in zip(range(1,6), accidents):
		ax.annotate( "({0},{1})".format(point[0], point[1]), xy = point, textcoords = "data")

	plt.xlabel("number of vehicles in accident")
	plt.ylabel("Number of accidents")
	plt.grid()

	plt.show()

def num_vehicle_cause():
	"""
		finds most often cause of accidents for a certain number of vehicles involved in accident
	"""
	# vehicle1_acc = pd.DataFrame(columns=data.columns)
	# vehicle2_acc = pd.DataFrame(columns=data.columns)
	# vehicle3_acc = pd.DataFrame(columns=data.columns)
	# vehicle4_acc = pd.DataFrame(columns=data.columns)
	# vehicle5_acc = pd.DataFrame(columns=data.columns)
	
	# for obs_idx, obs_data in data.iterrows():
	# 	pass

	print(data["CONTRIBUTING FACTOR VEHICLE 1"].unique())
	print("***********")
	print(data["CONTRIBUTING FACTOR VEHICLE 2"].unique())
	print("***********")
	print(data["CONTRIBUTING FACTOR VEHICLE 3"].unique())
	print("***********")
	print(data["CONTRIBUTING FACTOR VEHICLE 4"].unique())
	print("***********")
	print(data["CONTRIBUTING FACTOR VEHICLE 5"].unique())

def func():

	#print(type(data.loc[0, "CONTRIBUTING FACTOR VEHICLE 5"]))

	print(data["CONTRIBUTING FACTOR VEHICLE 1"].unique())# == "nan")


def main():
	get_overall_stats()

	get_heat_map()

	get_acc_hour()

	vehicles_involved()

if __name__ == "__main__":
	print(data.index)
	vehicles_involved()
	#func()