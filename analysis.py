import pandas as pd
import numpy as np

from util import readfile

data = readfile("bronx.csv")

print(data[np.logical_and(data.MONTH == 7, data.YEAR == 2017)])