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

def kml_generation(lat, lon):
	"""
		Given a list of latitude and longitude generates KML file for visualization on google earth.
		Name of KML file is bronx_location.kml

		:param lat: list of latitude values
		:param lon: list of longitude values
	"""
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
	    </Style>\n\
	    <Placemark><styleUrl>#yellowPoly</styleUrl>\n\
	    <LineString>\n\
	    <Description>Speed in MPH, not altitude.</Description>\n\
	    <extrude> 1 </extrude>\n\
	    <tesselate> 1 </tesselate>\n\
	    <altitudeMode> clamp to ground </altitudeMode>\n\
	    <coordinates>'
	for i in range(len(lat)):
		mystr = mystr + "\t\t" + str(lon[i]) + "," + str(lat[i]) + "\n"
	mystr = mystr + '</coordinates>\n </LineString>\n </Placemark>\n </Document>\n </kml>'
	file = open("bronx_location.kml", "w")
	file.write(mystr)
	file.close()
