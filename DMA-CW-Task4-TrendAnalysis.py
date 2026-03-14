#Trend Analysis
import pandas as pd #library for data sets - allow for use of functions such as .readcsv()
import matplotlib.pyplot as plt #library to plot graphs - plt.command

database = pd.read_csv("dataset.csv") #accesses csv file

#re-usable function that finds range
def calculations(variable):
    global weekdayValues,weekendValues #defined as globals so I can use them in draw function
    weekday = database[database["day_type"]=="Weekday"] #filters database by values where column day_type is Weekday
    weekend = database[database["day_type"]=="Weekend"] #filters database by values where column day_type is Weekend
    weekdayValues = weekday[variable].mean() #calculates mean of traffic flow where day_type is Weekday
    weekendValues = weekend[variable].mean() #calculates mean of traffic flow where day_type is Weekend
    return f"Variable:{variable}\nWeekday Mean:{weekdayValues}\nWeekend Mean:{weekendValues}\n" #returns all values

print(calculations("traffic_flow")) #passes string/column "traffic_flow" through function calculations, variable = "traffic_flow"

#function used to draw graph - barchart
def draw():
    #barchart
    fig, figure = plt.subplots() #creates figure
    barX = ['Weekday','Weekend'] #x axis data plots
    barY = [weekdayValues,weekendValues] #y axis data plots
    figure.bar(barX,barY) #creates bar chart .bar(x,y)
    plt.title("Bar Chart of Weekday and Weekend Traffic Flow") #graph title
    plt.xlabel("Day Type") #label x axis
    plt.ylabel("Traffic Flow (Vehicles Per Hour)") #label y axis
    plt.show() #displays graph

    #Line plot
    region = database[database["region"]=="South"].reset_index(drop=True) #filters database by values where region is South

    plt.plot(region.index, region["pm25"], marker="o") #plots line graph .plot(x,y)
    plt.title("PM25 Levels over Time in the South Region") 
    plt.xlabel("Time (1 day intervals)")
    plt.ylabel("PM25 (micrograms/m^3)")
    plt.show() #displays graph

draw() #calls function