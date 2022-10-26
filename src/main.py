import pandas
import numpy
import json

path = "../data/gtfs3Sept/"
file = "agency.txt"

df = pandas.read_csv(path+file)
df2 = pandas.read_json("../data/vehiclePosition01.json")
print(df.head())
print(df2.head())