#Solving Systems of Equations (P=0.5T+0.3N)
import pandas as pd #library for data sets - allow for use of functions such as .readcsv()
import matplotlib.pyplot as plt #library to plot graphs - plt.command

database = pd.read_csv("dataset.csv") #accesses csv file

#re-usable function that finds mean
def calculations(variable):
    mean = database[variable].mean() #calculates mean of the variable
    return f"Variable:{variable}\nMean:{mean}" #returns all values

print(calculations("traffic_flow")) #passes string/column "traffic_flow" through function calculations, variable = "traffic_flow"
print(calculations("noise"))
print(calculations("pm25"))