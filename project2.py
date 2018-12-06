import csv
import pandas as pd

def readfile(filename):
    data = pd.read_csv(filename, delimiter=',')
    return data

def data_cleaning(data):
    newfile = "Bronx.csv"
    new_data = data[(data.BOROUGH == 'BRONX')]
    new_data = new_data.drop("BOROUGH", axis=1)
    new_data = new_data.drop("LOCATION", axis=1)
    print(new_data.shape)
    new_data.to_csv(newfile)

def main():
    data = readfile("NYPD_Motor_Vehicle_Collisions.csv")
    data_cleaning(data)

if __name__ == '__main__':
    main()