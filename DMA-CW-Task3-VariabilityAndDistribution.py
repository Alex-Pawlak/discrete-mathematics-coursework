#Variability And Distribution
import pandas as pd #library for data sets - allow for use of functions such as .readcsv()
import matplotlib.pyplot as plt #library to plot graphs - plt.command

database = pd.read_csv("dataset.csv") #accesses csv file

#re-usable function that finds range
def calculations(variable):
    maximum = database[variable].max() #stores max value in variable maximum
    minimum = database[variable].min() #stores minimum value in variable minimum
    variable_range = maximum - minimum #calculates range
    return f"Variable:{variable}\nRange:{variable_range}\n" #returns all values

print(calculations("traffic_flow")) #passes string/column "traffic_flow" through function calculations, variable = "traffic_flow"
print(calculations("noise")) #passes string/column "noise" through function calculations, variable = "noise"

#function used to draw graph - histogram
def draw(variable):
    plt.figure(figsize=(10, 6)) #defines height and width
    database[variable].dropna().plot(kind="hist", bins=22, edgecolor="black") #bins means intervals, plots histogram
    plt.title(f"Histogram of {variable}") #graph title
    plt.xlabel(variable) #label x axis with variable name
    plt.ylabel("Frequency") #label y axis with Frequency
    plt.show() #displays graph

draw("noise") #calls function
