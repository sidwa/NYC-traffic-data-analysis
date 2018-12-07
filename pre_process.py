import csv
import pandas as pd
import numpy as np

from util import readfile

def parse_date(date_str, date_part):
	"""
		Converts date string to it's components in intger

		:param date_str: date string
		:param data_part: part of the date needed{day, month, year}

		:return: required part of the date
	"""
	date_str = date_str.replace("-", "/")
	date_str = date_str.strip().split("/")
	month_idx = 0
	day_idx = 1
	year_idx = 2
	date = {}
	date["month"] = int(date_str[month_idx])
	date["day"] = int(date_str[day_idx])
	date["year"] = int(date_str[year_idx])

	return date[date_part]

def parse_time(time_str, time_part):
	"""
		Converts time string to it's components in intger

		:param date_str: time string
		:param data_part: part of the time needed{hour, minute}

		:return: required part of the time
	"""
	time_str = time_str.strip().split(":")
	hr_idx = 0
	min_idx = 1
	time = {}
	time["hour"] = int(time_str[hr_idx])
	time["minute"] = int(time_str[min_idx])

	return time[time_part]

def data_cleaning(data):
	"""
		Takes the uncleaned data and performs operations to make it
		amenable for data analysis. Writes the data frame to a file
		in csv format 

		:param data: Pandas data frame containing required data of NY accidents
	"""
	newfile = "bronx.csv"
	# get rows with accidents in Bronx
	new_data = data[(data.BOROUGH == 'BRONX')]

	# remove borough and location cols not useful
	# for analysis
	new_data = new_data.drop("BOROUGH", axis=1)
	new_data = new_data.drop("LOCATION", axis=1)

	#nominal attribute removed
	new_data = new_data.drop("UNIQUE KEY", axis=1)
	
	# add separate columns for day, date and month for easier filtering.
	new_data["MONTH"] = new_data["DATE"].apply(parse_date, date_part = "month")
	new_data["DAY"] = new_data["DATE"].apply(parse_date, date_part = "day")
	new_data["YEAR"] = new_data["DATE"].apply(parse_date, date_part = "year")
	
	#add separate column for hour and min
	new_data["HOUR"] = new_data["TIME"].apply(parse_time, time_part = "hour")
	new_data["MINUTE"] = new_data["TIME"].apply(parse_time, time_part = "minute")

	#drop the Date and Time columns cz redundant now.
	new_data = new_data.drop("DATE", axis = 1)
	new_data = new_data.drop("TIME", axis = 1)

	#Data is now in 1 normal form.

	# pandas require numpy logical op functions for logical and/or operations
	new_data = new_data[np.logical_and(np.logical_or(new_data.MONTH == 7, new_data.MONTH == 8), \
		np.logical_or(new_data.YEAR == 2017, new_data.YEAR == 2018 ))]
	new_data.to_csv(newfile)

def main():
	data = readfile("data_set.csv")
	data_cleaning(data)

if __name__ == '__main__':
	main()