import pandas as pd
import numpy as np

from util import readfile

data = readfile("bronx.csv")
print("Total accidents:", data.shape[0])
print("Accidents in June 2017: ", data[np.logical_and(data.MONTH == 6, data.YEAR == 2017)].shape[0])
print("Accidents in July 2017: ", data[np.logical_and(data.MONTH == 7, data.YEAR == 2017)].shape[0])
print("Accidents in June 2018: ", data[np.logical_and(data.MONTH == 6, data.YEAR == 2018)].shape[0])
print("Accidents in July 2018: ", data[np.logical_and(data.MONTH == 7, data.YEAR == 2018)].shape[0])