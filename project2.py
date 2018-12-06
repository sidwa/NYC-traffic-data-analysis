import csv
import pandas as pd

def readfile(filename):
    data = pd.read_csv(filename, delimiter=',')
    return data

def data_cleaning(data):
    newfile = "Bronx.csv"
    fileobject = open(newfile, "w")
    new_data = data[(data.BOROUGH == 'BRONX')]
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        fileobject.write(str(new_data))




def main():
    data = readfile("NYPD_Motor_Vehicle_Collisions.csv")
    data_cleaning(data)

if __name__ == '__main__':
    main()