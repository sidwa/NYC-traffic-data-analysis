import numpy as np


def parse_date(date_str):
	date_str = date_str.replace("-", "/")
	date_str = date_str.strip().split("/")
	month_idx = 0
	date_idx = 1
	year_idx = 2
	date = {}
	date["month"] = int(date_str[month_idx])
	date["date"] = int(date_str[date_idx])
	date["year"] = int(date_str[year_idx])

	return date




def split_data(fname = "data_set.csv"):
	"""
		gets data from file and splits it into smaller
		datasets to be be further exmained.
		

		:param fname: file name from which to fetch data

		:return Tuple: -list of attributes 
					   -list of list of only data values

	"""
	data = []
	jn7 = open("june_2017.csv","w")
	jn8 = open("june_2018.csv", "w")
	jl7 = open("july_2017.csv", "w")
	jl8 = open("july_2018.csv", "w")
	c = open("common.csv", "w")
	with open(fname,"r") as f:  
		#  open("june_2017.csv","w") as jn7, \
		#  open("june_2018.csv", "w") as jn8, \
		#  open("july_2017.csv","w") as jl7, \
		#  open("july_2018.csv") as jl8, \
		#  open("common.csv") as c:

		#reads in the attribute list
		attr = f.readline().strip().split(",")

		date_attr_idx = 0
		borough_attr_idx = 2

		for file_num, data_line in enumerate(f):
			vals = data_line.strip().split(",")

			# All values in dataset are int so safe 
			# type conversion
			try :
				date = parse_date(vals[date_attr_idx])
			except ValueError :
				print("error at:", file_num)
				print(vals[date_attr_idx])
				print("value", date)
				exit()
			if vals[borough_attr_idx] == "BRONX":
				if date["month"] == 6 and date["year"] == 2017:
					jn7.write(data_line)
				elif date["month"] == 6 and date["year"] == 2018:
					jn8.write(data_line)
				elif date["month"] == 7 and date["year"] == 2017:
					jl7.write(data_line)
				elif date["month"] == 7 and date["year"] == 2018:
					jl8.write(data_line)
				elif ( date["month"] == 7 or date["month"] == 7 ) and ( date["year"] == 2017 or date["year"] == 2018 ):
					c.write(data_line)

	print("done")

if __name__ == "__main__":
	split_data()
