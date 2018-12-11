__author__ = "Shachi Amitkumar Turakhia, Siddhant Reddy"

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


def kml_generation(filename, lat, long):
	count = 0.0
	count = float(count)
	mystr = ''
	mystr = mystr + '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns = "http://www.opengis.net/kml/2.2">\n\
	    <Document>\n\
	    <Style id="yellowPoly">\n\
	        <LineStyle>\n\
	            <color>Af00ffff</color>\n\
	            <width>6</width>\n\
	        </LineStyle>\n\
	        <PolyStyle>\n\
	            <color>7f00ff00</color>\n\
	        </PolyStyle>\n\
	    </Style>\n'

	for i in range(len(lat)):
		mystr = mystr + '<Placemark>\n\
	                <description>Default Pin is Yellow</description>\n\
	                <Point>\n\
	                <coordinates>' + str(long[i]) + ", " + str(lat[i]) + ", " + str(count) + '</coordinates>\n\
	                </Point>\n\
	                </Placemark>'
	mystr = mystr + '</Document>\n </kml>'
	file = open(filename, "w")
	file.write(mystr)
	file.close()
