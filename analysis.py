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
	kml_generation("bronx_location.kml", lat, lon)



# =============Getting number of accidents by the hour stats=======================================
def get_acc_hour(data, plot = True):
	hours = range(24)
	num_accidents = []
	# get the number of accident for each hour of the day.
	# 23:59 is hour 23 and so is 23:00
	for hour in hours:
		num_accidents.append(data[data.HOUR == hour].shape[0])
	
	if plot:
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

	return (hours, num_accidents)

# =======================================vehicles involved============================================
def vehicles_involved(data, plot=True):
	"""
		finds number of accidents involving 1,2,3,4 and 5 vehicles.

		:param data: dataframe to work on, must conform with NYPD accident data set.
		:param plot: True if the results have to be plot

		:return: list with number of accidents for diff number of vehicles involved as indices.
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

	if plot:
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
	
	return accidents

def get_data_n_vehicles(data, num_vehicles):
	"""
		gets subset of data frame which has num_vehicles involved in the accident.

		:param num_vehicles: number of vehicles involved in the accident.
	"""
	bin_data = data.isnull()
	res = pd.DataFrame(columns=data.columns)
	for obs_idx, obs_data in data.iterrows():
		# if num_vehicle cell has value then check further
		if bin_data.loc[obs_idx, "CONTRIBUTING FACTOR VEHICLE " + str(num_vehicles)]:
			for i in range(num_vehicles + 1,6):
				# check if more than num_vehicles were involved
				if bin_data.loc[obs_idx, "CONTRIBUTING FACTOR VEHICLE " + str(i)]:
					#print("break")
					break
			else:
				# more vehicles were not involved, add to new data frame
				#print("add")
				#print(obs_data)
				res.loc[data.index.max() + 1] = obs_data
				print(data.index)
	
	return res

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

def get_acc_cause_time(hour, plot = True):
	"""
		get statitics of accidents given hour of the day
	"""

	dat = data[data.HOUR == hour]
	
	dat1 = get_data_n_vehicles(dat, 1)
	dat1 = dat1.dropna(subset=["CONTRIBUTING FACTOR VEHICLE 1"])
	print(dat1["HOUR"])
	print(dat1["CONTRIBUTING FACTOR VEHICLE 1"].unique())#value_counts().max())

	dat2 = get_data_n_vehicles(dat, 2)
	dat2 = dat2.dropna(subset=["CONTRIBUTING FACTOR VEHICLE 2"])
	print(dat2["CONTRIBUTING FACTOR VEHICLE 2"].value_counts().max())

	dat3 = get_data_n_vehicles(dat, 3)
	dat3 = dat3.dropna(subset=["CONTRIBUTING FACTOR VEHICLE 3"])
	print(dat3["CONTRIBUTING FACTOR VEHICLE 3"].value_counts().max())

	dat4 = get_data_n_vehicles(dat, 4)
	dat4 = dat4.dropna(subset=["CONTRIBUTING FACTOR VEHICLE 4"])
	print(dat4["CONTRIBUTING FACTOR VEHICLE 4"].value_counts().max())

	dat5 = get_data_n_vehicles(dat, 5)
	dat5 = dat5.dropna(subset=["CONTRIBUTING FACTOR VEHICLE 5"])
	print(dat5["CONTRIBUTING FACTOR VEHICLE 5"].value_counts().max())

	return vehicles_involved(dat, plot)

def acc_time_vehicle():
	"""
		find number of accidents w/ number of vehicles involved in accident with different time of day.
	"""
	acc = []
	num_vehicles_involved = 5
	colors = ["red", "green", "blue", "orange", "cyan"]
	for num_vehicles_involved in range(5,0,-1):
		acc = []
		for hour in range(24):
			acc.append(get_acc_cause_time(hour, False)[num_vehicles_involved-1])

		plt.plot(range(24), acc, c = colors[num_vehicles_involved-1], label = "Vehicles:" + str(num_vehicles_involved))
	
	plt.legend()
	plt.show()

def func():

	#print(type(data.loc[0, "CONTRIBUTING FACTOR VEHICLE 5"]))

	print(data["CONTRIBUTING FACTOR VEHICLE 1"].unique())# == "nan")


def main():
	get_overall_stats()

	get_heat_map()

	#get number of acc hour by hour for entire data set.
	get_acc_hour(data)

	#get number of acc hour by hour for june 2017
	get_acc_hour(data[np.logical_and(data.MONTH==6, data.YEAR==2017)])

	#get number of acc hour by hour for june 2018
	get_acc_hour(data[np.logical_and(data.MONTH==6, data.YEAR==2018)])

	#get number of acc hour by hour for july 2017
	get_acc_hour(data[np.logical_and(data.MONTH==7, data.YEAR==2017)])

	#get number of acc hour by hour for july 2018
	get_acc_hour(data[np.logical_and(data.MONTH==7, data.YEAR==2018)])

	vehicles_involved(data)

	acc_time_vehicle()

if __name__ == "__main__":
	#print(data.index)
	#vehicles_involved()
	#func()
	
	acc = []

	get_acc_cause_time(14)


	#************get month by month comparison of hourly accident stats **********
	# # get number of acc hour by hour for june 2017
	# acc.append(data[np.logical_and(data.MONTH==6, data.YEAR==2017)])

	# #get number of acc hour by hour for june 2018
	# acc.append(data[np.logical_and(data.MONTH==6, data.YEAR==2018)])

	# #get number of acc hour by hour for july 2017
	# acc.append(data[np.logical_and(data.MONTH==7, data.YEAR==2017)])

	# #get number of acc hour by hour for july 2018
	# acc.append(data[np.logical_and(data.MONTH==7, data.YEAR==2018)])

	# for i in range(len(acc)):
	# 	if i == 0:
	# 		hours, accidents = get_acc_hour(acc[i], False)
	# 		plt.plot(hours, accidents, label = "June 17")
		
	# 	if i == 1:
	# 		hours, accidents = get_acc_hour(acc[i], False)
	# 		plt.plot(hours, accidents, label = "June 18")

	# 	if i == 2:
	# 		hours, accidents = get_acc_hour(acc[i], False)
	# 		plt.plot(hours, accidents, label = "July 17")

	# 	if i == 3:
	# 		hours, accidents = get_acc_hour(acc[i], False)
	# 		plt.plot(hours, accidents, label = "July 18")

	# plt.legend()
	# plt.show()
	
	