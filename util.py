import pandas as pd
import numpy as np
import csv


def readfile(filename):
	"""
		Reads data from a csv file to create a pandas dataframe

		:param filename: name of file to be imported

		:return: pandas dataframe containing the data of the given file.
	"""
	data = pd.read_csv(filename, delimiter=',', low_memory=False)
	return data

